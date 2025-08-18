# food_recommender_final.py
import streamlit as st
import random

# 음식 데이터 (모든 조건 커버 + mood 추가)
foods = [
    # --- 한식 ---
    {"name": "김치찌개", "category": "한식", "spicy": True, "soup": True, "mood": "든든하게"},
    {"name": "불고기", "category": "한식", "spicy": False, "soup": False, "mood": "특별하게"},
    {"name": "비빔밥", "category": "한식", "spicy": True, "soup": False, "mood": "가볍게"},
    {"name": "갈비탕", "category": "한식", "spicy": False, "soup": True, "mood": "든든하게"},

    # --- 중식 ---
    {"name": "짬뽕", "category": "중식", "spicy": True, "soup": True, "mood": "든든하게"},
    {"name": "짜장면", "category": "중식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "마라탕", "category": "중식", "spicy": True, "soup": True, "mood": "특별하게"},
    {"name": "탕수육", "category": "중식", "spicy": False, "soup": False, "mood": "특별하게"},

    # --- 일식 ---
    {"name": "라멘", "category": "일식", "spicy": False, "soup": True, "mood": "든든하게"},
    {"name": "초밥", "category": "일식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "돈까스", "category": "일식", "spicy": False, "soup": False, "mood": "특별하게"},
    {"name": "가라아게 우동", "category": "일식", "spicy": False, "soup": True, "mood": "든든하게"},

    # --- 양식 ---
    {"name": "토마토 스프", "category": "양식", "spicy": False, "soup": True, "mood": "가볍게"},
    {"name": "스테이크", "category": "양식", "spicy": False, "soup": False, "mood": "특별하게"},
    {"name": "파스타", "category": "양식", "spicy": False, "soup": False, "mood": "든든하게"},
    {"name": "햄버거", "category": "양식", "spicy": False, "soup": False, "mood": "가볍게"},

    # --- 분식 ---
    {"name": "떡볶이", "category": "분식", "spicy": True, "soup": True, "mood": "가볍게"},
    {"name": "순대국밥", "category": "분식", "spicy": False, "soup": True, "mood": "든든하게"},
    {"name": "김밥", "category": "분식", "spicy": False, "soup": False, "mood": "가볍게"},
    {"name": "치즈라볶이", "category": "분식", "spicy": True, "soup": True, "mood": "특별하게"},
]

st.set_page_config(page_title="음식 추천기", page_icon="🍜", layout="centered")

st.title("🍜 오늘 뭐 먹지? 맞춤 음식 추천기")

# 질문 1: 매운 음식?
spicy_choice = st.radio("매운 음식이 땡기나요?", ["상관없음", "매운거 좋아요 🌶️", "순한게 좋아요 😌"])

# 질문 2: 국물 있는 음식?
soup_choice = st.radio("국물이 필요하신가요?", ["상관없음", "국물 있는 게 좋아요 🍲", "국물 없는 게 좋아요 🍙"])

# 질문 3: 음식 종류
category_choice = st.selectbox("어떤 종류가 먹고 싶으신가요?", ["상관없음", "한식", "중식", "일식", "양식", "분식"])

# 질문 4: 오늘 기분
mood_choice = st.radio("오늘 기분은 어떤가요?", ["상관없음", "가볍게", "든든하게", "특별하게"])

if st.button("추천 받기 🎲"):
    # 조건 필터링
    candidates = foods

    if spicy_choice != "상관없음":
        candidates = [f for f in candidates if f["spicy"] == (spicy_choice == "매운거 좋아요 🌶️")]

    if soup_choice != "상관없음":
        candidates = [f for f in candidates if f["soup"] == (soup_choice == "국물 있는 게 좋아요 🍲")]

    if category_choice != "상관없음":
        candidates = [f for f in candidates if f["category"] == category_choice]

    if mood_choice != "상관없음":
        candidates = [f for f in candidates if f["mood"] == mood_choice]

    if candidates:
        choice = random.choice(candidates)
        st.success(f"👉 오늘의 추천 음식은 **{choice['name']}** 입니다! 😋")
    else:
        st.error("조건에 맞는 음식이 없어요 😢 다시 선택해보세요!")
