from openai import OpenAI
import os
import sys

API_KEY = 'replace with your API key'

model_id = 'gpt-4' # replace with your model ID

os.environ["OPENAI_API_KEY"] = API_KEY

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

messages = []
messages.append({'role': 'system', 'content': 'How may I help you?'})

def ChatGPT_conversation(conversation):
    response = client.chat.completions.create(
        model=model_id,
        messages=conversation
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply


def get_bot_response(style):
    userText = f"""
Generate me more instructions like this, use in-content learning, keep similar length and similar style of instructions:
"Make this image {style} style."
"Change the image to {style} style."
"Make the image in {style} style."
"Apply {style} style to this image."
"Transform image into {style} art."
"Convert image to {style} style."
"Restyle image to {style} look."
"""
    messages.append({'role': 'user', 'content': userText})
    return str(ChatGPT_conversation(messages))

def get_bot_response_2nd_time(style):
    userText = f"""
    Give me 50 more instructions like this"""
    messages.append({'role': 'user', 'content': userText})
    return str(ChatGPT_conversation(messages))

style = sys.argv[1]
response_1 = get_bot_response(style)
response_2 = get_bot_response_2nd_time(style)
with open(f'gpt_response_{style}.txt', 'a') as f:
    for response in response_1.split('\n'):
        f.write(response + '\n')
    f.write('\n')
    for response in response_2.split('\n'):
        f.write(response + '\n')