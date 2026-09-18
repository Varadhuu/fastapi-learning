from groq import AsyncGroq
from ..config import settings

client = AsyncGroq(api_key=settings.groq_api_key)

async def generate_response(user_message: str) -> str:
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": user_message}],
        model=settings.model
    )
    return completion.choices[0].message.content