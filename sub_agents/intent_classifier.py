from google.adk import Agent

IntentClassifier = Agent(
    name="intent_classifier",
    model="gemini-2.0-flash",
    description="Classifies user intent for routing to the correct sub-agent.",
    instruction=(
        "You are an intent classifier. Given a user request, respond with one of: 'email', 'calendar', 'social', 'device', 'document', 'voice', or 'unknown'. "
        "Base your answer only on the user's intent. Respond with a single word."
    ),
    tools=[]
)
