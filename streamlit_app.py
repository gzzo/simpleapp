import time

time.sleep(10)

import streamlit as st
import os
import os.path
import secrets_helper

a = {}
print(a[st.secrets['secret_key']])

st.title("your secret")

with open(".streamlit/secrets.toml") as f:
  st.text(f.read())

st.json(dict(os.environ))
