```python
import openai
from config import CHATGPT_API_KEY

class ChatGPTHandler:
    def __init__(self):
        self.api_key = CHATGPT_API_KEY
        self.openai = openai.OpenAI(self.api_key)

    def generate_message(self, prompt, max_tokens=100):
        response = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']

    def review_code(self, code_diff):
        prompt = f"Review the following code differences:\n{code_diff}\nFocus on principles of clean code and software craftsmanship."
        return self.generate_message(prompt)
```