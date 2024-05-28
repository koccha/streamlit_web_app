import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import chardet



def detect_encoding(file):
    rawdata = file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    file.seek(0)  # ファイルポインタを先頭に戻す
    return encoding

# タイトルの表示
st.title("プライスターASIN抽出アプリ")

with  st.form(key="oppai"):

    # テキストエリアの表示
    text_area_input = st.text_area("ASINリスト", height=300)

    # 入力をリストに変換
    asin_list = text_area_input.split('\n')
    asin_list = [asin.strip() for asin in asin_list if asin.strip()]


    # ファイルアップロードのウィジェット
    uploaded_file = st.file_uploader("CSVファイルを選択してください", type=["csv"])

    # ボタン
    submit_btn = st.form_submit_button("送信")

    # ファイルがアップロードされた場合
    if submit_btn:
        # エンコードの検出
        encoding = detect_encoding(uploaded_file)
        
        # CSVファイルをデータフレームとして読み込み
        df_priceter_x = pd.read_csv(uploaded_file, encoding=encoding)

        # 不要な装飾文字を削除
        df_priceter_x["SKU"] = df_priceter_x["SKU"].str.lstrip('="').str.rstrip('"')
        df_priceter_x["ASIN"] = df_priceter_x["ASIN"].str.lstrip('="').str.rstrip('"')

        df = df_priceter_x[(df_priceter_x["ASIN"].isin(asin_list))]
        
        # データフレームの表示
        st.write("アップロードしたCSVファイルの内容:")
        st.dataframe(df)







