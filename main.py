# mbti_celeb_card_app.py
import streamlit as st

# MBTI별 대표 연예인 데이터 (3명씩)
mbti_celebrities = {
    "INTJ": [
        {"name": "아이유", "desc": "섬세하고 창의적인 아티스트", "image": "https://www.google.com/imgres?q=%EC%95%84%EC%9D%B4%EC%9C%A0&imgurl=https%3A%2F%2Fi.namu.wiki%2Fi%2FR0AhIJhNi8fkU2Al72pglkrT8QenAaCJd1as-d_iY6MC8nub1iI5VzIqzJlLa-1uzZm--TkB-KHFiT-P-t7bEg.webp&imgrefurl=https%3A%2F%2Fnamu.wiki%2Fw%2F%25EC%2595%2584%25EC%259D%25B4%25EC%259C%25A0&docid=nzo3Fzovz85czM&tbnid=JAo-iKIHAIC5BM&vet=12ahUKEwiLl7vDnYmPAxVcm1YBHUDlHkIQM3oECBIQAA..i&w=1000&h=1500&hcb=2&itg=1&ved=2ahUKEwiLl7vDnYmPAxVcm1YBHUDlHkIQM3oECBIQAA"},
        {"name": "박서준", "desc": "전략적이고 목표 지향적인 배우", "image": "https://i.imgur.com/p5tQqXo.jpg"},
        {"name": "정은지", "desc": "분석적이면서 감성적인 뮤지션", "image": "https://i.imgur.com/vmO9rS2.jpg"}
    ],
    "ENFP": [
        {"name": "박보검", "desc": "열정과 긍정 에너지가 가득한 배우", "image": "https://i.imgur.com/3zM7YOb.jpg"},
        {"name": "유노윤호", "desc": "카리스마 넘치는 에너자이저", "image": "https://i.imgur.com/d6Ilrwe.jpg"},
        {"name": "김세정", "desc": "활발하고 매력적인 뮤지션", "image": "https://i.imgur.com/yGQHhFt.jpg"}
    ],
    "INFJ": [
        {"name": "뷔 (BTS)", "desc": "감성적이고 비전 있는 예술가", "image": "https://i.imgur.com/T1hQbLB.jpg"},
        {"name": "수지", "desc": "따뜻하고 사람을 이끄는 배우", "image": "https://i.imgur.com/p3HHzpU.jpg"},
        {"name": "전종서", "desc": "섬세한 감정을 표현하는 배우", "image": "https://i.imgur.com/9z3NfOh.jpg"}
    ],
    "ISTP": [
        {"name": "이정재", "desc": "냉철하고 실용적인 배우", "image": "https://i.imgur.com/bYQtNED.jpg"},
        {"name": "송중기", "desc": "침착하면서도 유연한 배우", "image": "https://i.imgur.com/9RcywJd.jpg"},
        {"name": "김다미", "desc": "도전적이고 독창적인 배우", "image": "https://i.imgur.com/08Zf1fr.jpg"}
    ]
}

st.set_page_config(page_title="MBTI 성격별 대표 연예인", page_icon="🎭", layout="wide")

st.title("🎭 MBTI 성격별 대표 연예인")
st.write("당신의 MBTI를 선택하면 해당 성격의 대표 연예인 3명을 카드 형식으로 소개합니다!")

# CSS 카드 스타일
st.markdown("""
<style>
.card {
    display: inline-block;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    padding: 15px;
    margin: 10px;
    width: 280px;
    text-align: center;
}
.card img {
    border-radius: 10px;
    width: 100%;
    height: 250px;
    object-fit: cover;
}
.card h4 {
    margin-top: 10px;
    margin-bottom: 5px;
}
.card p {
    font-size: 14px;
    color: #555555;
}
</style>
""", unsafe_allow_html=True)

# MBTI 선택
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", list(mbti_celebrities.keys()))

# 카드 출력
cols = st.columns(3)
for i, celeb in enumerate(mbti_celebrities[selected_mbti]):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div class="card">
                <img src="{celeb['image']}" alt="{celeb['name']}">
                <h4>{celeb['name']}</h4>
                <p>{celeb['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
