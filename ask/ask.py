from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

messages = [
    {"role": "system", "content": "You are a concise, friendly assistant!"}
]

def chat(messages):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    reply = response.choices[0].message.content
    return reply, response.usage.prompt_tokens

try: 
    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "quit":
            print("Bye!")
            break

        messages.append({"role": "user", "content": user_input})

        reply, prompt_tokens = chat(messages)        
        print(f"Bot: {reply}")
        print(f" [messages: {len(messages)} | prompt_tokens: {prompt_tokens}]")

        messages.append({"role": "assistant", "content": reply})
except KeyboardInterrupt:
    print("\nBye!")