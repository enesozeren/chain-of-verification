from openai import OpenAI
from dotenv import load_dotenv
import os

CHAT_AGENT_MODEL_NAME = "gpt-4o-mini"
MAX_TOKENS=512
TEMPERATURE=0.5

class CoveAgent:
    def __init__(self):
        load_dotenv()
        self.openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def generate_response(self, system_instruction: str, query: str) -> str:
        prompt = [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": query}
        ]

        response = self.openai_client.chat.completions.create(
            model=CHAT_AGENT_MODEL_NAME,
            messages=prompt,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE
        )

        answer = response.choices[0].message.content.strip()
        return answer