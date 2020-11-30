import time

time.sleep(10)

import streamlit as st
import os

st.title("your secret")

with open("../secrets/secrets.toml") as f:
  st.text(f.read())

st.json(dict(os.environ))
