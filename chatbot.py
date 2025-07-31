from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
client = OpenAI()


MODEL="gpt-3.5-turbo"



class ChatBot:
    temperature = 0

    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def get_completion_from_messages(self, messages, model="gpt-3.5-turbo"):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=self.temperature
        )

        return response.choices[0].message.content

    def change_temperature(self, value):
        if 0 <= value <= 1:
            self.temperature = value
        else:
            raise ValueError("Temperature must be between 0 and 1.")