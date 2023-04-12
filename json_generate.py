import os
import openai
from api_key import API_key

def getResponse(user_prompt):

  openai.api_key = API_key

  prompt = user_prompt

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= [
      {"role": "user", "content": user_prompt}
      ],      
    temperature= 0
    )
      
  return response['choices'][0]['message']['content']


def create():
  with open('input.txt', 'r') as f:
      # Initialize an empty dictionary
      my_dict = {}

      for line in f:
          
          key, value = line.strip().split(': ')

          my_dict[key] = (int)(value)


  print(my_dict)

  goal_dict = {1: "cardio", 2: "muscle toning", 3: "ab development", 4: "biscep muscle development", 5: "leg muscle development", 6: "general muscle development"}
  experience_dict = {1: "no experience", 2: "some experience", 3: "extensive experience"}
  gym_dict = {1: "the gym", 2: "home"}

  

  user_prompt = f"Can you please generate a 4-week, {my_dict['days_per_week']} days per week workout plan for someone whose weight is {my_dict['weight']} pounds, has a height of {my_dict['height']} inches, and whose goal for the workout is {goal_dict[my_dict['goal']]}. They have {experience_dict[my_dict['experience']]} with workouts, with {my_dict['time_available']} hours available per day to workout, and will do the workouts at {gym_dict[my_dict['location']]}. Please specify the day of the week by name. At the end please give guidance on what types of food to eat and what types of food to avoid. In your answer, format everything as a json dict file."

  print(user_prompt)


  workout_suggestion = getResponse(user_prompt)
  print(workout_suggestion)

  f = open("output.json", "w")
  f.write(workout_suggestion)


