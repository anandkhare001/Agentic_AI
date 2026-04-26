from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.team import Team

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

web_agent=Agent(
    name="Web Agent",
    role="search the web for information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGoTools()],
    instructions=["Always include the sources"],
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools()],
    instructions=["Use tables to display data"],
    markdown=True,
)

# Team Agent
team = Team(
    name="Research Team",
    members=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Delegate to the appropriate agent based on the request.", "Always include sources", "Use tables to display data"]
)

team.print_response("What are the trending AI stories and how is NVDA stock doing?", stream=True)