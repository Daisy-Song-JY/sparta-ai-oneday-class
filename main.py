import streamlit as st
import time  ##시간 재서 명령어
from openai import OpenAI

# 코드스니펫 - 제목
st.title('나만의 제품 홍보 생성기')

# 코드스니펫 - 입력
keyword = st.text_input("키워드를 입력하세요.")

# 코드스니펫 - 버튼
if st.button('실행'):
  st.write('원고 작성 완료')
  # 코드스니펫 - 스피너   (if 절 안에 넣어서 버튼 눌러야 타임스피너 뜨도록)
  with st.spinner('Wait for it...'):

    #여기에 chat-gpt에서 카피를 뽑아주는 API 호출하는 코드 삽입

    client = OpenAI(api_key=st.secrets["API_KEY"])  #open AI 연결

    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": keyword +
            '라는 주제로 새로운 홍보 문구 카피 20자 이내',  #여기를 바꿔 적으면 질문이 달라지니 다른 답을 뱉음
        }],
        model="gpt-4o",
    )

    chat_result = chat_completion.choices[0].message.content
    #print(chat_result)  ##이건 콘솔에 나오는 화면
    # 코드스니펫 - 글쓰기

    st.write(chat_result)

    #여기에 dalle에서 카피를 뽑아주는 API 호출하는 코드 삽입

    response = client.images.generate(
        model="dall-e-3",
        prompt=keyword,  #여기를 수정하면 뱉는 이미지 바뀜
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    # 코드스니펫 - 이미지
    st.image(image_url)

    time.sleep(5)  ## 5초동안 정지해있어라
  st.success('Done!')
