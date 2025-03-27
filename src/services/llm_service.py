from groq import Groq
import instructor
from pydantic import BaseModel
from config import Config

client = Groq(api_key=Config.GROQ_API_KEY, )

client = instructor.from_groq(client)

def interact(messages: list, model: str, response_model = None) -> dict:
    """
    Handles multi-turn conversation by maintaining history and generating responses.

    Args:
        messages (list): The conversation history.

    Returns:
        str: The assistant's response.
    """
    response = client.chat.completions.create(
        messages=messages,
        model=model,
        response_model=response_model,
        
        
    )
    return response.dict()