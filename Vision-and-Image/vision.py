from dotenv import load_dotenv
# loading environment variables from .env file
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini model and get responses
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)

    return response.text

# initialize streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")

input = st.text_input("Input Prompt : ", key = "input")
uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"], accept_multiple_files=False)
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image.", use_column_width=True)

submit = st.button("Submit")

if submit:
    response = get_gemini_response(input, image)
    st.write(response)