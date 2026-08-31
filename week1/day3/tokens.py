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
prompt1="Hi"
prompt2="Explain laptop"
prompt3="Explain Tablet not the medicine one"

prompts=[prompt1, prompt2, prompt3]
for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages, max_tokens=50)
    usage=response.usage
    print(
        f"Prompt: {prompt} --> "
        f"Prompt tokens: {usage.prompt_tokens}, "
        f"Completion tokens: {usage.completion_tokens}, "
        f"Total tokens: {usage.total_tokens},"
        f"Finish Reason: {response.choices[0].finish_reason}"
    )

# message={
#     "role":role,
#     "content":prompt1
# }

# messages=[message]

# response=client.chat.completions.create(model=model, messages=messages)

# answer=response.choices[0].message.content
# print(answer)