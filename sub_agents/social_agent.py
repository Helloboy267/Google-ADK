from google.adk import Agent
import tools

SocialAgent = Agent(
    name="social_agent",
    model="gemini-2.0-flash",
    description="Handles all social media tasks.",
    instruction=(
        "You are the Social Media Agent. Respond only to social media queries. "
        "Always use accessible formatting."
    ),
    tools=[tools.post_to_social]
)
