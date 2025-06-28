from google.adk import Agent
import tools

WhatsAppBusinessAgent = Agent(
    name="whatsapp_business_agent",
    model="gemini-2.0-flash",
    description="Handles WhatsApp Business messaging and automation.",
    instruction=(
        "You are the WhatsApp Business Agent. Respond only to WhatsApp Business-related queries. "
        "Always use accessible formatting."
    ),
    tools=[tools.manage_whatsapp_business]
)
