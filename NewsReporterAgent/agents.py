from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from tools import tool

load_dotenv()

## call the gemini model
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-preview-05-20",
                             verbose = True,
                             temperature= 0.5,
                             google_api_key = os.getenv("GOOGLE_API_KEY"))

# creating a senior researcher agent with memory and verbose mode
news_researcher = Agent(
    role = "Seniro Researcher",
    goal = "Uncover ground breaking technologies in {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = True
)

## creating a write agent with custom tools responsible in writing news blog
news_writer = Agent(
    role = "writer",
    goal = "Narrate compelling tech stories about {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "with a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools = [tool],
    llm = llm,
    allow_delegation = False
)
