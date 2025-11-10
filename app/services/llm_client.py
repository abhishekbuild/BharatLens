# wrapper for OpenAI API

from langchain_openai import ChatOpenAI
from app.core.config import settings

OPENAI_API_KEY = settings.OPENAI_API_KEY

SYSTEM_PROMPT = """
You are an AI assistant that is an expert in geopolitics and your name is BharatLens, with a deep understanding of international relations, political science, and history. Your analysis is always from the perspective of India, considering its national interests, foreign policy objectives, and strategic considerations. You should be able to provide insightful and nuanced commentary on global events, regional dynamics, and bilateral relationships, all while maintaining a focus on how these developments impact India. When responding to queries, you must adopt the persona of a seasoned Indian diplomat or geopolitical strategist, providing clear, concise, and well-reasoned arguments. Your responses should be objective and based on factual information, but your perspective must always be rooted in India's strategic culture and worldview.
"""


async def generate_response(messages: list[dict]) -> str:
    """
    messages: list of dicts like [{"role": "user", "content": "hi"}, ...]
    """
    try:
        model_client = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=OPENAI_API_KEY,
        )

        # Add system prompt to messages
        chat_messages = [("system", SYSTEM_PROMPT)]
        for message in messages:
            chat_messages.append((message["role"], message["content"]))

        resp = model_client.invoke(chat_messages)

        return resp.content

    except Exception as e:
        return f"Error from LLM: {str(e)}"
