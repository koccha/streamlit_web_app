import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import chardet


st.title("Spread Sheetフィルター関数")
st.caption("リストの重複は自動でカットされるから便利")


with  st.form(key="spreadsheet_func"):
    # 列
    alph = st.text_input("列アルファベット")
    # テキストエリアの表示
    text_area_input = st.text_area("ASIN or JANリスト", height=300)

    # ボタン
    submit_btn = st.form_submit_button("送信")

    if submit_btn:
        # 入力をリストに変換
        asin_list = text_area_input.split('\n')
        asin_list = [asin.strip() for asin in asin_list if asin.strip()]
        asin_list = list(set(asin_list))
        asin_list_shaped = "|".join(asin_list)

        # 結果
        st.write(f'=REGEXMATCH({alph}\:{alph},"{asin_list_shaped}") ')








