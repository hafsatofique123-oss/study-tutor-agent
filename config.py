import os

from crewai import LLM


MODEL_NAME = "groq/openai/gpt-oss-120b"


def get_llm():
    """Create and return the Groq LLM used by the Study Tutor Agent."""

    if not os.environ.get("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY is not configured.")

    return LLM(
        model=MODEL_NAME,
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=0.3,
    )
