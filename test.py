# food_recommender.py
import streamlit as st
import random

# 음식 리스트 (원하는 만큼 추가 가능)
foods = {
    "한식": ["김치찌개", "불고기", "비빔밥", "삼겹살", "된장찌개", "치킨"],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "꿔바로우"],
    "일식": ["초밥", "라멘", "돈까스", "우동", "덮밥"],
    "양식": ["피자", "파스타", "스테이크", "햄버거", "리조또"],
    "분식": ["떡볶이", "순대", "김밥", "라볶이", "오뎅"]
}

st.set_page_config(page_title="랜덤 음식 추천기", page_icon="🍽️", layout="centered")

st.title("🍽️ 오늘 뭐 먹지? 랜덤 음식 추천기")

# 음식 카테고리 선택
category = st.selectbox("먹고 싶은 음식 종류를 선택하세요!", ["전체"] + list(foods.keys()))

if st.button("추천 받기 🎲"):
    if category == "전체":
        # 모든 카테고리에서 랜덤
        all_foods = sum(foods.values(), [])
        choice = random.choice(all_foods)
    else:
        choice = random.choice(foods[category])
    
    st.success(f"👉 오늘의 추천 음식은 **{choice}** 입니다! 😋")
