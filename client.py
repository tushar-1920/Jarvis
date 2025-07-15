from openai import OpenAI

# pip install openai
# If you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
