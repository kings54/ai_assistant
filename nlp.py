# nlp.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']
