from google.adk import Agent
import tools

CalendarAgent = Agent(
    name="calendar_agent",
    model="gemini-2.0-flash",
    description="Handles all calendar-related tasks.",
    instruction=(
        "You are the Calendar Agent. Respond only to calendar-related queries. "
        "Always use accessible formatting."
    ),
    tools=[tools.manage_calendar]
)
