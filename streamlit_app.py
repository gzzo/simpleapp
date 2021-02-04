import streamlit as st

st.title("lfs test 1")

with open("moo.psd") as f:
    st.text(f.read())


