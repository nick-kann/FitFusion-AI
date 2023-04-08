import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def landmark_coord(landmark):
    return np.array([landmark.x, landmark.y])

def find_angle(a, b, c):
    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)

# For webcam input:
is_up = False
down_count = 0
up_count = 0
rep_count = 0
cap = cv2.VideoCapture(0)
frame_count = cv2.CAP_PROP_FPS
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
    if results.pose_landmarks is not None:
        # Extract pose landmarks
        landmarks = results.pose_landmarks.landmark

        nose = landmark_coord(landmarks[mp_pose.PoseLandmark.NOSE.value])
        left_wrist = landmark_coord(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])
        right_wrist = landmark_coord(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])
        left_shoulder = landmark_coord(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value])
        right_shoulder = landmark_coord(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value])

        if (left_wrist[1] > nose[1] and right_wrist[1] > nose[1]):
            up_count += 1
            if up_count > int(frame_count / 3):
                is_up = True
                down_count = 0

        if (left_wrist[1] < left_shoulder[1] and right_wrist[1] < right_shoulder[1]):
            down_count += 1
            if down_count > int(frame_count / 3):
                if (is_up == True):
                    rep_count += 1
                    print(rep_count)
                is_up = False
                up_count = 0

    if cv2.waitKey(5) & 0xFF == 27: # esc to quit
      break
cap.release()
