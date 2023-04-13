import requests
import pyttsx3

API_URL = "https://0xtanmoysamanta-facebook-blenderbot-400m-distill.hf.space/run/predict"
headers = {"Content-Type": "application/json"}

engine = pyttsx3.init()

while True:
    user_input = input("You: ")
    if user_input.lower() == 'q':
        break

    response = requests.post(API_URL, headers=headers, json={
        "data": [
            user_input,
            None,
        ]
    }).json()

    chatbot_output = response['data'][0][-1][-1]

    print("Chatbot:", chatbot_output)

    # use pyttsx3 to speak the chatbot's response
    engine.say(chatbot_output)
    engine.runAndWait()

    duration = response['duration']
    print(f"Response generated in {duration} seconds.")
