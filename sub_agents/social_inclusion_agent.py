from google.adk import Agent
import tools

SocialInclusionAgent = Agent(
    name="social_inclusion_agent",
    model="gemini-2.0-flash",
    description="Helps users join communities, summarize social media, and find events.",
    instruction=(
        "You are the Social Inclusion Agent. Help users join communities, summarize social media, and find accessible events. Always use accessible formatting."
    ),
    tools=[tools.social_inclusion_helper]
)
