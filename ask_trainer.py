import os
import openai
from api_key import API_key


def getResponse(user_prompt):
    openai.api_key = API_key

    prompt = user_prompt

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_prompt}
        ],
        temperature = 1

    )

    return response['choices'][0]['message']['content']
    # print("Response {}: {}".format(i+1, response['choices'][0]['message']['content']))

def initialize(question):
    question = "What's the best potato chips to buy?"
    user_prompt = "You are to act as my personal trainer. I will ask you a question about fitness and exercise, and you will respond with a helpful answer. If my question is not about fitness and exercise, you will respond with \"As your personal trainer, I can only answer your fitness related questions.\" Limit your response to 2 to 3 sentences. The question is: " + question
    #print(user_prompt)

    workout_suggestion = getResponse(user_prompt)
    return(workout_suggestion)
