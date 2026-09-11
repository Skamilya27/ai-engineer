import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY key is missing")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-20b"
role="user"


from pydantic import BaseModel

class Ticket(BaseModel):
    name:str
    email: str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f"""
    Extract the personal information from the ticket strictly based on this schema and give me a json output.
    {schema}
"""

message_system={
    "role":"system",
    "content": system_prompt
}

text="Hello I am Suman, I have purchase an iphone recently which stopped working please check and reply me on mob no 988989888 and my email id is suman@gmail.com"
prompt = f"""
    This is a cutomer ticket. Please extract the personal details from this.
    {text}
"""
# prompt1="Hi"
# prompt2="Explain laptop"
# prompt3="Explain Tablet not the medicine one"

# prompts=[prompt1, prompt2, prompt3]
# for prompt in prompts:
#     message={
#         "role":role,
#         "content":prompt
#     }
#     messages=[message]
#     response=client.chat.completions.create(model=model, messages=messages, max_tokens=50)
#     usage=response.usage
#     print(
#         f"Prompt: {prompt} --> "
#         f"Prompt tokens: {usage.prompt_tokens}, "
#         f"Completion tokens: {usage.completion_tokens}, "
#         f"Total tokens: {usage.total_tokens},"
#         f"Finish Reason: {response.choices[0].finish_reason}"
#     )

message={
    "role":role,
    "content":prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer=response.choices[0].message.content
print(answer)

import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket)

