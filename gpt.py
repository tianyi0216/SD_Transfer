from openai import OpenAI
import os
import sys

API_KEY = 'Replace with your API key'

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


def get_ai_response(style, input_caption):
    userText = f"""
    Given the following pairs, use in-content learning to generate a single-line output caption that describes the {input_caption} in the style of {style}:
    Input: {input_caption}
    Output: {input_caption} in {style} style.

    Input: {input_caption}
    Output: In {style} style, {input_caption}.

    Input: {input_caption}
    Output: {style} style of {input_caption}.

    Input: {input_caption}
    Output: {input_caption} in the style of {style}.

    In your output, only include the caption that describes the {input_caption} in the style of {style}, do not include input or any other information.
    """
    messages.append({'role': 'user', 'content': userText})
    return str(ChatGPT_conversation(messages))

style = sys.argv[1]
input_caption = sys.argv[2]
fname = sys.argv[3]
response_1 = get_ai_response(style, input_caption)
# with open(f'gpt_response_{style}.txt', 'a') as f:
#     for response in response_1.split('\n'):
#         f.write(response + '\n')
#     f.write('\n')
#     for response in response_2.split('\n'):
#         f.write(response + '\n')


with open(f'{fname}.txt', 'w') as f:
    for response in response_1.split('\n'):
        f.write(response + '\n')