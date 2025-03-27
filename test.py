import os
from groq import Groq
import instructor
from pydantic import BaseModel

# Initialize with API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Enable instructor patches for Groq client
client = instructor.from_groq(client)


class User(BaseModel):
    name: str
    age: int


# Create structured output
user = client.chat.completions.create(
    model="llama3-groq-70b-8192-tool-use-preview",
    messages=[
        {"role": "user", "content": "Extract: Jason is 25 years old"},
    ],
    response_model=User,
)

print(user)
# > User(name='Jason', age=25)