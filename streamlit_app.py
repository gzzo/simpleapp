import time

time.sleep(10)

import streamlit as st
import os

st.title("your secret")

st.text(os.getcwd())
st.text(os.expanduser('~'))

with open("../secrets/secrets.toml") as f:
  st.text(f.read())

st.json(dict(os.environ))
