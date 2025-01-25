from openai import OpenAI

client = OpenAI(api_key="")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "recommends movies"},
        {"role": "user", "content": "나 영화 추천 해줄래?"},
    ],
)

print(response.choices[0].message.content)
