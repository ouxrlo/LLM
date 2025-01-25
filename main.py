from openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일 에서 환경 변수 로드
load_dotenv()

# API Key 설정
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# prompt 명령
prompt = "Recommend movies."

# 초기 대화 설정
message = [{"role": "system", "content": prompt}]

# 대화 내용 저장 파일 설정
chat_file = "movie_chat.txt"


while True:
    user_input = input("user: ")

    if user_input.lower() == "exit":
        print("Good bye")
        break

    message.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=message)

    ai_response = response.choices[0].message.content

    print("AI: " + ai_response)

