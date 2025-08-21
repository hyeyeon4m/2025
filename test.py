import streamlit as st
import random

# 음식 데이터
foods = [
    {"name": "김치찌개", "category": "한식", "spicy": True, "soup": True, "mood": "든든하게"},
    {"name": "콩국수", "category": "한식", "spicy": False, "soup": True, "mood": "특별하게"},
    {"name": "불고기", "category": "한식", "spicy": False, "soup": False, "mood": "특별하게"},
    {"name": "국밥", "category": "한식", "spicy": False, "soup": True, "mood": "든하게"},
    {"name": "육회", "category": "한식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "비빔밥", "category": "한식", "spicy": True, "soup": False, "mood": "가볍게"},
    {"name": "김치볶음밥", "category": "한식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "갈비탕", "category": "한식", "spicy": False, "soup": True, "mood": "특별하게"},
    {"name": "된장찌개", "category": "한식", "spicy": False, "soup": True, "mood": "든든하게"},
    {"name": "짬뽕", "category": "중식", "spicy": True, "soup": True, "mood": "든든하게"},
    {"name": "짜장면", "category": "중식", "spicy": False, "soup": False, "mood": "든든하게"},
    {"name": "마라탕", "category": "중식", "spicy": True, "soup": True, "mood": "특별하게"},
    {"name": "탕수육", "category": "중식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "라멘", "category": "일식", "spicy": True, "soup": True, "mood": "든든하게"},
    {"name": "덮밥", "category": "일식", "spicy": False, "soup": False, "mood": "든든하게"},
    {"name": "초밥", "category": "일식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "돈까스", "category": "일식", "spicy": False, "soup": False, "mood": "특별하게"},
    {"name": "가라아게 우동", "category": "일식", "spicy": False, "soup": True, "mood": "든든하게"},
    {"name": "피자", "category": "양식", "spicy": False, "soup": False, "mood": "특별하게"},
    {"name": "스프", "category": "양식", "spicy": False, "soup": True, "mood": "가볍게"},
    {"name": "국수", "category": "한", "spicy": False, "soup": True, "mood": "가볍게"},
    {"name": "스테이크", "category": "양식", "spicy": False, "soup": False, "mood": "특별하게"},
    {"name": "파스타", "category": "양식", "spicy": False, "soup": False, "mood": "든든하게"},
    {"name": "햄버거", "category": "양식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "떡볶이", "category": "분식", "spicy": True, "soup": True, "mood": "가볍게"},
    {"name": "순대국밥", "category": "분식", "spicy": False, "soup": True, "mood": "든든하게"},
    {"name": "김밥", "category": "분식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "라면", "category": "분식", "spicy": True, "soup": True, "mood": "가볍게"},
    {"name": "치즈라볶이", "category": "분식", "spicy": True, "soup": True, "mood": "특별하게"}, ]

st.set_page_config(page_title="음식 추천기", page_icon="🍜", layout="centered")

# 버튼 스타일 + 첫 번째 옵션 숨기기
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #FF6347;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #e5533d;
        transform: scale(1.05);
    }
    /* 라디오 첫번째 옵션 숨기기 */
    div[role="radiogroup"] > label:first-child {
        display: none !important;
    }
    /* 셀렉트박스 첫번째 옵션 숨기기 */
    div[data-baseweb="select"] li[data-option-index="0"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🍜 오늘 뭐 먹지? 맞춤 음식 추천기")

# --- 옵션 선택 (숨김 + 상관없음 포함) ---
spicy_choice = st.radio(
    "매운 음식이 땡기나요?",
    ["-- 선택 안 함 --", "상관없음", "매운거 좋아요 🌶️", "순한게 좋아요 😌"],
    index=0
)

soup_choice = st.radio(
    "국물이 필요하신가요?",
    ["-- 선택 안 함 --", "상관없음", "국물 있는 게 좋아요 🍲", "국물 없는 게 좋아요 🍙"],
    index=0
)

mood_choice = st.radio(
    "오늘 기분은 어떤가요?",
    ["-- 선택 안 함 --", "상관없음", "가볍게", "든든하게", "특별하게"],
    index=0
)

category_choice = st.selectbox(
    "어떤 종류가 먹고 싶으신가요?",
    ["-- 선택 안 함 --", "상관없음", "한식", "중식", "일식", "양식", "분식"],
    index=0
)

# 선택 해석 함수
def clean_choice(choice):
    return None if choice.startswith("--") else choice

# --- 추천 로직 ---
if st.button("추천 받기 🎲"):
    candidates = foods

    spicy_val = clean_choice(spicy_choice)
    soup_val = clean_choice(soup_choice)
    mood_val = clean_choice(mood_choice)
    category_val = clean_choice(category_choice)

    if spicy_val and spicy_val != "상관없음":
        candidates = [f for f in candidates if f["spicy"] == (spicy_val == "매운거 좋아요 🌶️")]
    if soup_val and soup_val != "상관없음":
        candidates = [f for f in candidates if f["soup"] == (soup_val == "국물 있는 게 좋아요 🍲")]
    if category_val and category_val != "상관없음":
        candidates = [f for f in candidates if f["category"] == category_val]
    if mood_val and mood_val != "상관없음":
        candidates = [f for f in candidates if f["mood"] == mood_val]

    if candidates:
        choice = random.choice(candidates)
        st.success(f"👉 오늘의 추천 음식은 **{choice['name']}** 입니다! 😋")
        st.balloons()
    else:
        st.error("조건에 맞는 음식이 없어요 😢 다시 선택해보세요!")
        st.snow()
