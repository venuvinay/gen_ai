import os 
import google.generativeai as genai
import streamlit as st
os.environ["GOOGLE_API_KEY"] = "AIzaSyDNcL6xfGSSRRQVgbbDGHwHYG7PKC23O-k"
genai.configure(api_key = os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-pro")
def generate(input_text):
    response = model.generate_content(input_text)
    return response.text

st.title("VINAY -PRO  gpt")
input_text = st.text_input("Write your prompt")
if input_text:
    st.write(generate(input_text))