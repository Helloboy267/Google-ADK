from google.adk import Agent
import tools

WorkAgent = Agent(
    name="work_agent",
    model="gemini-2.0-flash",
    description="Assists with daily work, productivity, and accessible document/email management.",
    instruction=(
        "You are the Work Agent. Help users manage work, emails, meetings, and documents. Always use accessible formatting."
    ),
    tools=[tools.work_helper]
)
