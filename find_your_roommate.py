import streamlit as st
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
import os

matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams["font.family"] = 'NanumGothic'

csv_file_path = 'user_data.csv'

def load_data() :
    if os.path.exists(csv_file_path) :
        return pd.read_csv(csv_file_path)
    else :
        return pd.DataFrame(columns=["학년", "계열", "이름", "취미", "주로 자러가는 시간", "성향", "벌점"])

def save_data(df) :
    df.to_csv(csv_file_path, index=False)

st.title("Find_your_roommate")

grade = st.selectbox("당신의 학년을 선택하세요", [1, 2, 3])
college = st.selectbox("계열을 선택하세요", ['국내 문과', '국내 이과', '국제 문과', '국제 이과'])
name = st.text_input("이름을 입력하세요")
hobby = st.text_input("취미를 입력하세요")
sleep = st.slider("주로 자러가는 시간을 선택하세요 (참고* 16시 = 새벽 4시)", 9, 16, value = [10, 11])
extroverted = st.slider("자신의 성향을 선택하세요 (0이면 몹시 내향적, 10이면 몹시 외향적)", 0, 10, 5)
points = st.slider("자신의 벌점이 몇 점대인지 선택하세요", -20, 60, value=[0, 5], step = 5)

def append_input() :
    data = {
    "학년": [grade],
    "계열": [college],
    "이름" : [name],
    "취미": [hobby],
    "주로 자러가는 시간": [f"{sleep[0]}시 - {sleep[1]}시"],
    "성향": [extroverted],
    "벌점": [f"{points[0]}점 - {points[1]}점"]
    }
    df = pd.DataFrame(data)

    existing_data = load_data()

    updated_data = pd.concat([existing_data, df], ignore_index=True)

    save_data(updated_data)

    st.write("프로필 리스트")
    st.dataframe(updated_data, use_container_width=True)


if st.button("서버에 프로필 업로드") : 
    append_input()

st.write("프로필 리스트")
st.dataframe(load_data(), use_container_width=True)