from google.adk import Agent
import tools

HealthAgent = Agent(
    name="health_agent",
    model="gemini-2.0-flash",
    description="Reminds about medication, appointments, and health routines.",
    instruction=(
        "You are the Health Agent. Remind users about medication, appointments, and health routines. Always use accessible formatting."
    ),
    tools=[tools.health_helper]
)
