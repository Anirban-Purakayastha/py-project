from openai import OpenAI
client = OpenAI(
# assistant = client.beta.assistants.create(
#   name="Math Tutor",
#   instructions="You are a personal math tutor. Write and run code to answer math questions.",
#   tools=[{"type": "code_interpreter"}],
#   model="gpt-4o",
# )
    api_key=("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")
)
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)