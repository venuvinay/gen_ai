import os
import google.generativeai as genai
import streamlit as st
from PIL import Image
os.environ["GOOGLE_API_KEY"]="AIzaSyDNcL6xfGSSRRQVgbbDGHwHYG7PKC23O-k"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model=genai.GenerativeModel("gemini-1.5-pro")
def generate(image,promt):
    response=model.generate_content([image,promt])
    return response.text
st.title("image description")
image = st.file_uploader("Upload the image",type=["png","jpeg"])
input_text = st.text_input("enter the prompt for your image")
button = st.button("click for result")
if image and input_text and button:
    im = Image.open(image)
    st.image(im)
    st.write(generate(im,input_text))
