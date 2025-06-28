from google.adk import Agent
import tools

DocumentAgent = Agent(
    name="document_agent",
    model="gemini-2.0-flash",
    description="Handles document reading and summarization.",
    instruction=(
        "You are the Document Agent. Respond only to document-related queries. "
        "Always use accessible formatting."
    ),
    tools=[tools.read_document]
)
