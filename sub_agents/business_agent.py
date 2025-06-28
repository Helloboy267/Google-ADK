from google.adk import Agent
import tools

BusinessAgent = Agent(
    name="business_agent",
    model="gemini-2.0-flash",
    description="Assists with business tasks, analytics, and customer communication.",
    instruction=(
        "You are the Business Agent. Help users with business analytics, proposals, and customer communication. Always use accessible formatting."
    ),
    tools=[tools.business_helper]
)
