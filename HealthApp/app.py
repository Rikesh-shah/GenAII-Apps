import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

def get_gemini_response(input_prompt, image):
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type" : uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
## streamlit app
st.set_page_config(page_title="Health App")
st.header("Gemini Health App")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width = True)

submit = st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)