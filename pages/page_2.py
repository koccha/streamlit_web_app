import streamlit as st


with st.form(key="oppai"):
    # テキストボックス
    name = st.text_input("名前")
    address = st.text_input("住所")

    # セレクトボックス
    age_category = st.radio(
        "年齢層",
        ('こども', 'でっかいおっぱい')
    )

    # 複数選択
    hobby = st.multiselect(
        '趣味',
        ('おっぱい', 'すんごいおっぱい', 'いやーおっぱいでっか')
    )




    # ボタン
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル") 

# print(f"submit_btn: {submit_btn}")
# print(f"cancel_btn: {cancel_btn}")

if submit_btn:
    st.text(f"ようこそ{name}さん、{address}におっぱい！")
    st.text(f"{age_category}だね")
    st.text(f"趣味: {','.join(hobby)}")