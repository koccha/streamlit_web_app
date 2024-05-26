import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt


st.title("俺のアプリ")
st.caption("oppai")

# 画像
image = Image.open("./data/image1.jpg")
st.image(image)