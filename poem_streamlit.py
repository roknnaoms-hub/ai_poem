from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
import streamlit as st
import time

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

st.markdown(
    """
    <h1 style="
        color:#000080;
        text-align:center;
        margin-bottom:20px;
        font-weight:800;
        line-height:1.1;
        font-family:'Malgun Gothic', 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif;">
        <span style="font-size:40px; vertical-align:middle;">😎 </span>
        <span style="font-size:85px; vertical-align:middle;">AI</span>
        <span style="font-size:80px; vertical-align:middle;">시인</span>
        <span style="font-size:40px; vertical-align:middle;"> 😎</span>
    </h1>
    """,
    unsafe_allow_html=True
)

# 시 주제 : 입력 필드 (Input widgets -> TEXT -> st.text_input())
title = st.text_input("시의 주제를 입력하세요.")
st.write("시의 주제 :", title)

# 시작성 요청: 버튼 (Input widgets -> BUTTONS -> st.button()
if st.button("시 작성"):
  with st.spinner("Wait for it..."):
    #llm
    llm = init_chat_model(
    "gpt-5.4",
    api_key=api_key,
    temperature=0.7,
    )
    # 프롬프트 템플릿 생성
    prompt = ChatPromptTemplate.from_messages([
      ('system','너는 답변을 생성해주는 조력자'),
      ('user',"{input}")
    ])

    #출력 파서
    output_parser = StrOutputParser()
    
    #체인실행
    chain = prompt | llm | output_parser
    response = chain.invoke({"input":title+"에 시를 생성해줘"})
    print(response)
    

    st.write(response)

