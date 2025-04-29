from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
load_dotenv()
agent = Agent(
    model=Groq(id="compound-beta"),
    markdown=True,
    instructions=["Answer user queries using real-time info."]
)
agent.print_response("Fastest Centuries in IPL: List of Players", stream=True)
