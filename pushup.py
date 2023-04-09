import cv2
import mediapipe as mp
import numpy as np
import imageio


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

def start():
    # For webcam input:
    is_up = True
    down_count = 0
    up_count = 0
    rep_count = 0


    gif = imageio.mimread('./countdown_images/pushup_visual.gif')

    gif_frame = 0

    cap = cv2.VideoCapture(0)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(cv2.CAP_PROP_FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frames = 0
    countdown = 3
    countdown_complete = False
    start_countdown = False
    print("ready...")
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

        if cv2.waitKey(1) == ord(' '):
            start_countdown = True

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        cv2.flip(image, 1)

        if start_countdown and not countdown_complete:
            font_scale = 7
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_thickness = 24

            countdown_text = str(countdown) if countdown > 0 else "start!"
            text_size, _ = cv2.getTextSize(countdown_text, font, font_scale, font_thickness)
            text_size_x, text_size_y = text_size

            image = cv2.putText(image, countdown_text, ((width - text_size_x)//2, (height + text_size_y) //2), font,
                                    font_scale, (255, 255, 255), font_thickness, cv2.LINE_AA)

            frames += 1
            if frames >= fps:
                if countdown <= 0:
                    countdown_complete = True
                    print("start!")
                else:

                    frames = 0
                    print(countdown)
                    countdown -= 1

                # Flip the image horizontally for a selfie-view display.

        if not start_countdown:
            gif_image = cv2.cvtColor(gif[gif_frame], cv2.COLOR_BGR2RGB)

            gif_image = cv2.resize(gif_image, (image.shape[1], image.shape[0]))

            image = cv2.addWeighted(image, 0.5, gif_image, 0.5, 0)

            countdown_text = "Press space to start the countdown"
            text_size, _ = cv2.getTextSize(countdown_text, cv2.FONT_HERSHEY_SIMPLEX, 1, 3)
            text_size_x, text_size_y = text_size

            image = cv2.putText(image, countdown_text, ((width - text_size_x) // 2, (height - (4 * text_size_y)) // 2), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0, 0), 3, cv2.LINE_AA)

        cv2.imshow('the gif!', image)

        gif_frame +=2
        if gif_frame >= len(gif):
            gif_frame = 0

        if results.pose_landmarks is not None and countdown_complete:
            # Extract pose landmarks
            landmarks = results.pose_landmarks.landmark

            # pushup test

            left_shoulder = landmark_coord(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value])
            left_elbow = landmark_coord(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value])
            left_wrist = landmark_coord(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value])

            left_angle = find_angle(left_shoulder, left_elbow, left_wrist)


            right_shoulder = landmark_coord(landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value])
            right_elbow = landmark_coord(landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value])
            right_wrist = landmark_coord(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])

            right_angle = find_angle(right_shoulder, right_elbow, right_wrist)

            if (landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z < landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].z):
                test_angle = left_angle
            else:
                test_angle = right_angle


            if (test_angle <= 90):
                down_count += 1
                if (down_count >= 4):
                    up_count = 0
                    is_up = False
            if (test_angle >= 160):
                up_count += 1
                if (up_count >= 4):
                    down_count = 0
                    if (is_up == False):
                        rep_count += 1
                        print(rep_count)
                    is_up = True



        if cv2.waitKey(5) & 0xFF == 27: # esc to quit
          break
    cap.release()
    cv2.destroyAllWindows()
