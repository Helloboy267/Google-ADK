from google.adk import Agent
import tools

EducationAgent = Agent(
    name="education_agent",
    model="gemini-2.0-flash",
    description="Helps with accessible learning, summarizing textbooks, and explaining concepts.",
    instruction=(
        "You are the Education Agent. Help users learn, summarize, and explain educational content in accessible ways. Always use simple language and accessible formatting."
    ),
    tools=[tools.education_helper]
)
