from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

st.set_page_config(page_title="AI 시인", page_icon="😎", layout="centered")

api_key = st.secrets["OPENAI_API_KEY"]

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

title = st.text_input("시의 주제를 입력하세요.")
st.write("시의 주제 :", title)

if st.button("시 작성"):
    if not title.strip():
        st.warning("시의 주제를 먼저 입력하세요.")
    else:
        with st.spinner("시를 작성하는 중입니다..."):
            llm = init_chat_model(
                model="gpt-5.4",
                model_provider="openai",
                api_key=api_key,
                temperature=0.7,
            )

            prompt = ChatPromptTemplate.from_messages([
                ("system", "너는 한국어로 자연스럽고 감성적인 시를 작성하는 AI 시인이다."),
                ("user", "{input}")
            ])

            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser
            response = chain.invoke({"input": f"{title}에 대한 시를 생성해줘."})

            st.subheader("생성된 시")
            st.write(response)