from google.adk import Agent
import tools

VoiceAgent = Agent(
    name="voice_agent",
    model="gemini-2.0-flash",
    description="Handles voice commands and accessibility.",
    instruction=(
        "You are the Voice Agent. Respond only to voice command queries. "
        "Always use accessible formatting."
    ),
    tools=[tools.voice_command_handler]
)
