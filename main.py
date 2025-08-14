# mbti_appearance_fashion_full.py
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 외모·패션 특징", page_icon="👗", layout="centered")

# CSS 카드 스타일
st.markdown("""
    <style>
    .mbti-card {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .title {
        font-size: 28px;
        font-weight: bold;
        color: #333;
    }
    .subtitle {
        font-size: 18px;
        color: #555;
        margin: 5px 0 3px;
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 데이터 (전체 16개 유형 예시 — 이미지 일부만 채워짐)
mbti_data = {
    "INTJ": {
        "appearance": "차분하고 깔끔한 스타일, 시크한 표정, 단정한 헤어스타일을 선호.",
        "fashion": "미니멀한 블랙 코트, 슬림핏 팬츠, 간결한 디자인의 시계.",
        "celeb": {
            "name": "RM (방탄소년단)",
            "image": "https://commons.wikimedia.org/wiki/Special:FilePath/RM_in_the_Oval_Office_of_the_White_House%2C_May_31%2C_2022_%28cropped%29.jpg"
        }
    },
    "INTP": {
        "appearance": "편안한 옷차림, 무심한 듯 자연스러운 헤어, 부드러운 표정.",
        "fashion": "오버사이즈 셔츠, 와이드 팬츠, 심플한 운동화.",
        "celeb": {
            "name": "진 (방탄소년단)",
            "image": "https://example.com/jin.jpg"  # 실제 위키미디어 이미지 채워주세요
        }
    },
    "ENTJ": {
        "appearance": "자신감 있는 자세, 정돈된 스타일, 깔끔한 슈트나 포멀룩.",
        "fashion": "정장 코디, 날렵한 로퍼, 모던한 시계.",
        "celeb": {
            "name": "김연아",
            "image": "https://example.com/kim_yuna.jpg"
        }
    },
    "ENTP": {
        "appearance": "개성 강한 패션, 활발한 제스처, 다양한 표정.",
        "fashion": "컬러풀한 자켓, 패턴 셔츠, 유니크 스니커즈.",
        "celeb": {
            "name": "하하",
            "image": "https://example.com/haha.jpg"
        }
    },
    "INFJ": {
        "appearance": "부드럽고 차분한 표정, 따뜻한 눈빛,
