# mbti_appearance_fashion_app.py
import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 외모·패션 특징", page_icon="👗", layout="centered")

# CSS로 카드 스타일 추가
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
    }
    </style>
""", unsafe_allow_html=True)

# MBTI 데이터 (예시 4개, 나머지는 같은 형식으로 추가 가능)
mbti_data = {
    "INTJ": {
        "appearance": "차분하고 깔끔한 스타일, 시크한 표정, 단정한 헤어스타일을 선호.",
        "fashion": "미니멀한 블랙 코트, 슬림핏 팬츠, 간결한 디자인의 시계.",
        "celeb": {
            "name": "RM (방탄소년단)",
            "image": "https://upload.wikimedia.org/wikipedia/commons/2/26/RM_at_the_White_House%2C_May_2022.jpg"
        }
    },
    "ENFP": {
        "appearance": "화려한 표정, 트렌디한 스타일, 컬러풀한 패션.",
        "fashion": "비비드 컬러 재킷, 패턴 셔츠, 청바지, 스니커즈.",
        "celeb": {
            "name": "박보검",
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Park_Bo-gum_in_September_2016.png"
        }
    },
    "INFJ": {
        "appearance": "부드럽고 차분한 표정, 따뜻한 눈빛, 심플한 스타일.",
        "fashion": "베이지 트렌치코트, 니트 스웨터, 심플한 목걸이.",
        "celeb": {
            "name": "수지",
            "image": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Suzy_for_Marie_Claire_Korea_2017.png"
        }
    },
    "ISTP": {
        "appearance": "심플하면서 활동적인 스타일, 편안한 옷차림, 무심한 표정.",
        "fashion": "후드티, 조거팬츠, 스니커즈, 백팩.",
        "celeb": {
            "name": "이정재",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/87/Lee_Jung-jae_2022.jpg"
        }
    }
}

st.title("👗 MBTI 성격별 외모 & 패션 스타일")
st.write("MBTI별 전형적인 **외모 특징**, **어울리는 패션 스타일**, **대표 연예인**을 한 눈에 확인해보세요!")

# MBTI 선택
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", list(mbti_data.keys()))

# 결과 카드
if selected_mbti:
    info = mbti_data[selected_mbti_]()_
