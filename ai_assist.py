# Example: reuse your existing OpenAI client code
# Change the baseUrl to point to LM Studio
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://127.0.0.1:1234/v1",
                api_key="lm-studio")

completion = client.chat.completions.create(
  model="phi-4",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "Как тебя зовут?"}
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)

