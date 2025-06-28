from google.adk import Agent
import tools

LearningAgent = Agent(
    name="learning_agent",
    model="gemini-2.0-flash",
    description="Helps users find, summarize, and learn new skills or courses.",
    instruction=(
        "You are the Learning Agent. Help users find and learn new skills, summarize tutorials, and track progress. Always use accessible formatting."
    ),
    tools=[tools.learning_helper]
)
