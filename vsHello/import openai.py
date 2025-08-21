import openai

# OpenAI API 키 설정
try:
    with open("../_apikeys.env", "r") as key_file:
        for line in key_file:
            if line.startswith("Emma3rdkey="):
                openai.api_key = line.split("=", 1)[1].strip()
                break
        else:
            raise Exception("파일에 'OPENAI_API_KEY'가 정의되어 있지 않습니다.")
except FileNotFoundError:
    raise Exception("키 파일(_apikey.env)을 찾을 수 없습니다. 파일을 생성하고 'OPENAI_API_KEY'를 추가하세요.")

def chat_with_gpt(prompt):
    """
    OpenAI GPT 모델에 프롬프트를 전달하고 응답을 반환합니다.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # 사용할 모델 엔진
            prompt=prompt,
            max_tokens=150,  # 응답의 최대 토큰 수
            temperature=0.7,  # 창의성 조정
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("OpenAI GPT와 대화하세요! (종료하려면 'exit' 입력)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("대화를 종료합니다.")
            break
        response = chat_with_gpt(user_input)
        print(f"GPT: {response}")
