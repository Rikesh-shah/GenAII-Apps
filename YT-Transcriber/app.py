import os
import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def get_gemini_response(transcript_text,prompt):
    response = model.generate_content(prompt+transcript_text)
    return response.text

## getting the transcript from the yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]

        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript =""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    
    except Exception as e:
        raise e
    
## streamlit app
st.set_page_config(page_title="Youtube Video Summarizer")
st.header("Gemini Youtube Video Summarizer")

youtube_link = st.text_input("Enter youtube link : ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=get_gemini_response(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)