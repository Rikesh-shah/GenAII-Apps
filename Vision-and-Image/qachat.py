import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
chat = model.start_chat(history = [])

def get_gemini_response(prompt):
    response = chat.send_message(prompt, stream = True)
    return response

# initialize the streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input : ", key = "input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    # add user query and respone to chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is :")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Gemini", chunk.text))

st.subheader("The chat History is : ")

for role, text in st.session_state['chat_history']:
    st.write(f"{role} : {text}")