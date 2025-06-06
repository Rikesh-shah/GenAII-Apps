import google.generativeai as genai
import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.5-flash-preview-05-20')
def get_gemini_response(input, image, user_prompt):
    response = model.generate_content([input, image[0], user_prompt])
    return response.text

def input_image_detail(uploaded_file):
    if uploaded_file is not None:
        # read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type" : uploaded_file.type,   # Get the mime type of the uploaded file
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file founded")

# initialize streamlit app
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")

input = st.text_input("Input prompt : ", key = "input")
uploaded_file = st.file_uploader("Choose an image of the invoice...", type = ['jpg', 'jpeg', 'png'])

image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the Invoice.")

input_prompt = """
You are an expert in understanding invoices. We will upload a image as invoices
and you will have to answer any questions based on the uploaded invoice image
"""

if submit:
    image_data = input_image_detail(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The response is ")
    st.write(response)