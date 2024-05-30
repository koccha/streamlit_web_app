import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import chardet



# テキストエリアの表示
text_area_input = st.text_area("ASINリスト", height=300)

# 入力をリストに変換
asin_list = text_area_input.split('\n')
asin_list = [asin.strip() for asin in asin_list if asin.strip()]
df_asin_list = pd.DataFrame(asin_list, columns=["ASIN"])
st.dataframe(df_asin_list)