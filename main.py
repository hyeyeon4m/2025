# mbti_celeb_app.py
import streamlit as st

# MBTI별 대표 연예인 데이터
mbti_celebrities = {
    "INTJ": {"name": "아이유", "desc": "섬세하고 창의적인 아티스트", "image": "https://i.imgur.com/6Xq0xD1.jpg"},
    "INTP": {"name": "RM (방탄소년단)", "desc": "지적이고 분석적인 리더", "image": "https://i.imgur.com/W3yzs9F.jpg"},
    "ENTJ": {"name": "유재석", "desc": "타고난 리더십과 추진력", "image": "https://i.imgur.com/3qj2K3V.jpg"},
    "ENTP": {"name": "하하", "desc": "창의적이고 유쾌한 분위기 메이커", "image": "https://i.imgur.com/7Up5pXx.jpg"},
    "INFJ": {"name": "방탄소년단 뷔", "desc": "감성적이고 비전 있는 예술가", "image": "https://i.imgur.com/T1hQbLB.jpg"},
    "INFP": {"name": "태연", "desc": "따뜻하고 이상주의적인 뮤지션", "image": "https://i.imgur.com/OlBkKxM.jpg"},
    "ENFJ": {"name": "수지", "desc": "사람들을 이끄는 카리스마와 따뜻함", "image": "https://i.imgur.com/p3HHzpU.jpg"},
    "ENFP": {"name": "박보검", "desc": "열정과 긍정 에너지가 가득한 배우", "image": "https://i.imgur.com/3zM7YOb.jpg"},
    "ISTJ": {"name": "정해인", "desc": "성실하고 책임감 있는 배우", "image": "https://i.imgur.com/RD5PGfA.jpg"},
    "ISFJ": {"name": "손예진", "desc": "따뜻하고 헌신적인 배우", "image": "https://i.imgur.com/ZuQq1XJ.jpg"},
    "ESTJ": {"name": "김희애", "desc": "실용적이고 조직적인 배우", "image": "https://i.imgur.com/L5kV5Jt.jpg"},
    "ESFJ": {"name": "유리 (소녀시대)", "desc": "친화력과 배려심이 돋보이는 배우", "image": "https://i.imgur.com/KSP2uOl.jpg"},
    "ISTP": {"name": "이정재", "desc": "냉철하고 실용적인 배우", "image": "https://i.imgur.com/bYQtNED.jpg"},
    "ISFP": {"name": "지수 (블랙핑크)", "desc": "감성적이고 유연한 아티스트", "image": "https://i.imgur.com/9Qy8X9o.jpg"},
    "ESTP": {"name": "이광수", "desc": "즉흥적이고 에너지 넘치는 배우", "image": "https://i.imgur.com/Rn6V3M8.jpg"},
    "ESFP": {"name": "김세정", "desc": "즐겁고 매력적인 에너자이저", "image": "https://i.imgur.com/yGQHhFt.jpg"}
}

st.set_page_config(page_title="MBTI 성격별 대표 연예인", page_icon="🎭")

st.title("🎭 MBTI 성격별 대표 연예인")
st.write("당신의 MBTI를 선택하면 해당 성격을 가진 대표 연예인을 소개합니다!")

# MBTI 선택
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", list(mbti_celebrities.keys()))

# 결과 출력
if selected_mbti:
    celeb = mbti_celebrities[selected_mbti]
    st.subheader(f"{selected_mbti} - {celeb['name']}")
    st.image(celeb["image"], width=300)
    st.write(celeb["desc"])
