import streamlit as st

st.title("main app")

value = st.slider("Pick a number", 0, 10, 3)

st.write(value)

input = st.text_input("Tell me something", "Cantami o Diva")

with open("temp_file.txt", "a") as f:
  f.write(f"{input}\n")
  
with open("temp_file.txt", "r") as f:
  st.write(f.read())

st.write("Streamlit is fabulous")

st.write("Hello Corey, this is the demo!")
st.balloons()

print("this is a log line")

uploaded_file = st.file_uploader("Choose a Jpg file", type="jpg")
if uploaded_file is not None:
    st.write(uploaded_file)
