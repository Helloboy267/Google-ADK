from google.adk import Agent
import tools

TravelAgent = Agent(
    name="travel_agent",
    model="gemini-2.0-flash",
    description="Assists with travel, navigation, and booking rides.",
    instruction=(
        "You are the Travel Agent. Help users plan routes, book rides, and provide accessible navigation. Always use accessible formatting."
    ),
    tools=[tools.travel_helper]
)
