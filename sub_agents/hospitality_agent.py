from google.adk import Agent
import tools

HospitalityAgent = Agent(
    name="hospitality_agent",
    model="gemini-2.0-flash",
    description="Assists with booking, ordering, and hospitality services.",
    instruction=(
        "You are the Hospitality Agent. Help users book services, order food, and communicate with staff. Always use accessible formatting."
    ),
    tools=[tools.hospitality_helper]
)
