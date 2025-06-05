from dotenv import load_dotenv
# loading environment variables from .env file
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini model and get responses
model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

input = st.text_input("Input : ", key = "input")
submit = st.button("Submit")

# When submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is :")
    st.write(response)

