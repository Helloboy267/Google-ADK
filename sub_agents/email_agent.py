from google.adk import Agent
import tools

EmailAgent = Agent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Handles all email-related tasks.",
    instruction=(
        "You are the Email Agent. Respond only to email-related queries. "
        "Always use accessible formatting."
    ),
    tools=[tools.manage_emails]
)
