# API key website :- https://ai.google.dev/pricing

from dotenv import load_dotenv
load_dotenv() #loading all environment variables
import streamlit as st
import os
import google.generativeai as ai
from PIL import Image

# ai.configure(api_key="YOUR API KEY")
ai.configure(api_key=os.getenv("API_KEY"))


model = ai.GenerativeModel("gemini-pro-vision")

#function to load gemini pro model and return response

def gemini_response(query,image):
    if query != "":
        response = model.generate_content([query,image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit app code

st.set_page_config(page_title="Gemini Image BOT 🤖")

st.header("Gemini Image BOT 🤖")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

input = st.text_input("Input: ",key = "input")

submit = st.button(" ➡️ ")


if submit:
    response = gemini_response(input,image)
    st.write(response)