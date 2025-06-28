from google.adk import Agent
import tools

EarningAgent = Agent(
    name="earning_agent",
    model="gemini-2.0-flash",
    description="Helps users find jobs, manage freelance work, and automate earning tasks.",
    instruction=(
        "You are the Earning Agent. Help users find jobs, manage freelance work, and automate earning. Always use accessible formatting."
    ),
    tools=[tools.earning_helper]
)
