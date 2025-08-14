# mbti_appearance_app.py
import streamlit as st

# MBTI별 외모/분위기 특징 데이터
mbti_appearance = {
    "INTJ": "차분하고 깔끔한 스타일, 시크한 표정, 단정한 헤어스타일을 선호.",
    "INTP": "편안한 옷차림, 무심한 듯 자연스러운 헤어, 부드러운 표정.",
    "ENTJ": "자신감 있는 자세, 정돈된 스타일, 깔끔한 슈트나 포멀룩.",
    "ENTP": "개성 강한 패션, 활발한 제스처, 다양한 표정.",
    "INFJ": "부드럽고 차분한 표정, 따뜻한 눈빛, 심플한 스타일.",
    "INFP": "감성적인 분위기, 자연스러운 메이크업, 편안한 복장.",
    "ENFJ": "밝은 미소, 세련된 패션, 친근한 분위기.",
    "ENFP": "화려한 표정, 트렌디한 스타일, 컬러풀한 패션.",
    "ISTJ": "단정한 복장, 깔끔한 머리, 반듯한 인상.",
    "ISFJ": "따뜻하고 온화한 인상, 정갈한 스타일, 부드러운 색감.",
    "ESTJ": "깔끔하고 권위 있는 스타일, 단정한 헤어, 강한 인상.",
    "ESFJ": "밝고 친근한 표정, 부드러운 패션, 환한 미소.",
    "ISTP": "심플하면서 활동적인 스타일, 편안한 옷차림, 무심한 표정.",
    "ISFP": "감각적인 패션, 자연스러운 헤어, 부드러운 인상.",
    "ESTP": "스포티한 스타일, 자신감 있는 표정, 활동적인 이미지.",
    "ESFP": "화려하고 눈에 띄는 스타일, 큰 리액션, 생동감 있는 표정."
}

st.set_page_config(page_title="MBTI 외모 특징", page_icon="👀")

st.title("👀 MBTI 성격별 외모 특징")
st.write("당신의 MBTI를 선택하면 전형적인 외모·분위기 특징을 소개합니다!")

# MBTI 선택
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", list(mbti_appearance.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형의 외모 특징")
    st.write(mbti_appearance[selected_mbti])
