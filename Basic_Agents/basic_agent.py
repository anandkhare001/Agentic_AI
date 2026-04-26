from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


agent=Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=(
        "You are a helpful AI assistant. "
        "Answer clearly and concisely. "
        "Use DuckDuckGo tool when you need real-time or external information."
    ),
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Who won the T20 World Cup 2026")