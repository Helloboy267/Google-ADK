from google.adk import Agent
import tools

DeviceAgent = Agent(
    name="device_agent",
    model="gemini-2.0-flash",
    description="Handles smart home device control.",
    instruction=(
        "You are the Device Agent. Respond only to smart home device queries. "
        "Always use accessible formatting."
    ),
    tools=[tools.control_device]
)
