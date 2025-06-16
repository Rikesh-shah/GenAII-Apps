from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from tools import yt_tool

load_dotenv()

## call the gemini model
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-preview-05-20",
    verbose = True,
    temperature = 0.5,
    google_api_key = os.getenv("GOOGLE_API_KEY")
)


## Create a Senior Blog content researcher agent
blog_researcher = Agent(
    role = "Blog Researcher from youtube Videos.",
    goal = "Get the relevant video content for the topic {topic} from yt channel.",
    verbose = True,
    memory = True,
    back_story = (
        "Expert in understanding videos in AI Data science, Machine Learning and Gen AI and providing suggestion."
    ),
    tools = [yt_tool],
    llm = llm,
    allow_delegation = True
)

## create a senior blog writer agent with YT tool
blog_writer = Agent(
    role = "Senior Blog Writer.",
    goal = "Narrate compelling tech stories about the video {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools = [yt_tool],
    llm = llm,
    allow_delegation = False
)