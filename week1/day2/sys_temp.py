import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY key is missing")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"
role="user"
prompt="Explain laptop in 60 words"

message_system={
    "role":"system",
    "content":"explain it like you are my loving grandmother"
}

message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages, temperature=2)

answer=response.choices[0].message.content
print(answer)