import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options={"api_version": "v1"}
)

SYSTEM_PROMPT = """
You are VoiceAid AI, a voice-based assistant for rural users in India.
Answer in simple English.
Keep responses short and clear.
Only answer questions related to agriculture and government schemes.
"""

def generate_response(user_text: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

User question:
{user_text}

Answer:
"""

    response = client.models.generate_content(
        model="models/gemini-1.0-pro",
        contents=prompt
    )

    return response.text.strip()
