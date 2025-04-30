import asyncio
from langchain.tools import Tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from agentami.agents.ami import AgentAmi
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()  # Your .env file should contain OPENAI_API_KEY


# Step 1: Define some mock tools
@tool
def mock_tool_function():
    """
    makes halwa
    """
    return 'made halwa for the user'


tools = [
    mock_tool_function,
    Tool(name="WeatherTool", description="Provides current weather information based on location.",
         func=lambda x: "Weather info"),
    Tool(name="StockTool", description="Gives the latest stock prices and trends.", func=lambda x: "Stock info"),
    Tool(name="NewsTool", description="Fetches breaking news headlines worldwide.", func=lambda x: "News info"),
    Tool(name="CalculatorTool", description="Performs basic arithmetic calculations.", func=lambda x: str(eval(x))),
    Tool(name="CurrencyConverter", description="Converts currency from one unit to another.",
         func=lambda x: "Currency conversion"),
    Tool(name="ReminderTool", description="Sets reminders for events and tasks.", func=lambda x: "Reminder set"),
    Tool(name="FlightSearchTool", description="Helps find and book flights.", func=lambda x: "Flight options"),
    Tool(name="RecipeTool", description="Suggests recipes based on available ingredients.",
         func=lambda x: "Recipe suggestions"),
]

# Step 3: Create the agent instance
agent = AgentAmi(model=ChatOpenAI(model="gpt-4o"),
                 tools=tools,
                 checkpointer=InMemorySaver(),)

# Step 4: Compile the LangGraph
agent_ami = agent.graph

# Step 5: Run the agent interactively
async def run_graph():
    print("AgentAmi is ready. Type your queries. Type 'exit' to quit.")
    config = {"configurable": {"thread_id": "1"}}  # Example thread_id
    while True:
        prompt = input("\nQuery: ")
        if prompt.lower() in {"exit", "quit"}:
            break
        print("\n--- Response ---")
        async for event in agent_ami.astream({"messages": [("human", prompt)]}, stream_mode="updates",
                                             config=config):
            print(event)

asyncio.run(run_graph())
