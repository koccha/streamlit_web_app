import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt


df = pd.read_csv('./data/data.csv', index_col="月")
st.bar_chart(df["2021年"])

fig, ax = plt.subplots()
ax.plot(df.index, df["2021年"])
ax.set_title('matploclib graph')
st.pyplot(fig)