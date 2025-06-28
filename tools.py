import os
from google.adk.types import ToolContext, tool
from utils import make_accessible

@tool
def manage_emails(service: str, action: str, context: ToolContext) -> str:
    """Access and manage emails. Services: 'gmail' or 'outlook'. Actions: 'read', 'send', 'search'."""
    try:
        if service not in ('gmail', 'outlook'):
            return make_accessible("Sorry, only Gmail and Outlook are supported.")
        if action == 'read':
            # Placeholder: Simulate fetching top 3 unread emails
            emails = [
                {"from": "alice@example.com", "subject": "Meeting Update", "snippet": "The meeting is at 10 AM."},
                {"from": "bob@example.com", "subject": "Invoice", "snippet": "Please find attached invoice."},
                {"from": "carol@example.com", "subject": "Greetings", "snippet": "Hope you are well!"}
            ]
            summary = "Email Summary: You have 3 unread emails. "
            for i, email in enumerate(emails, 1):
                summary += f"Email {i}: From {email['from']}, Subject: {email['subject']}. {email['snippet']} "
            return make_accessible(summary)
        elif action == 'send':
            # Placeholder: Confirm before sending
            return make_accessible("Ready to send your email. Please confirm the recipient and message.")
        elif action == 'search':
            # Placeholder: Simulate search
            results = ["Subject: Project Plan", "Subject: Lunch Invitation"]
            return make_accessible("Search Results: " + ", ".join(results))
        else:
            return make_accessible("Sorry, that action is not supported.")
    except Exception:
        return make_accessible("I'm sorry, I couldn't access your emails right now. Please try again later.")

@tool
def manage_calendar(service: str, action: str, context: ToolContext) -> str:
    """Manage calendar events. Services: 'google' or 'outlook'. Actions: 'get', 'create', 'delete'."""
    try:
        if service not in ('google', 'outlook'):
            return make_accessible("Sorry, only Google and Outlook calendars are supported.")
        if action == 'get':
            # Placeholder: Simulate today's events
            events = [
                {"title": "Team Meeting", "time": "10 AM"},
                {"title": "Doctor Appointment", "time": "2 PM"},
                {"title": "Call with Alex", "time": "4 PM"}
            ]
            if not events:
                return make_accessible("Calendar Events: You have no events today.")
            summary = f"Calendar Events: You have {len(events)} events today. "
            for i, event in enumerate(events, 1):
                summary += f"Event {i}: '{event['title']}' at {event['time']}. "
            return make_accessible(summary)
        elif action == 'create':
            return make_accessible("Please provide the event details. I will confirm before creating it.")
        elif action == 'delete':
            return make_accessible("Please specify which event to delete. I will confirm before deleting.")
        else:
            return make_accessible("Sorry, that action is not supported.")
    except Exception:
        return make_accessible("I'm sorry, I couldn't access your calendar right now. Please try again later.")

@tool
def post_to_social(platform: str, message: str, context: ToolContext) -> str:
    """Post updates to social media. Platforms: 'twitter', 'facebook'."""
    try:
        if platform not in ('twitter', 'facebook'):
            return make_accessible("Sorry, only Twitter and Facebook are supported.")
        # Placeholder: Simulate posting
        return make_accessible(f"Posted to {platform.capitalize()} for you.")
    except Exception:
        return make_accessible("I'm sorry, I couldn't post to social media right now. Please try again later.")

@tool
def control_device(device_type: str, action: str, context: ToolContext) -> str:
    """Control smart devices. Types: 'light', 'thermostat'. Actions: 'on', 'off', 'adjust'."""
    try:
        if device_type not in ('light', 'thermostat'):
            return make_accessible("Sorry, only lights and thermostats are supported.")
        if action not in ('on', 'off', 'adjust'):
            return make_accessible("Sorry, that action is not supported.")
        # Placeholder: Simulate device control
        if device_type == 'light':
            return make_accessible(f"Okay, turning the light {action}.")
        elif device_type == 'thermostat':
            return make_accessible(f"Okay, setting the thermostat to the requested setting.")
    except Exception:
        return make_accessible("I'm sorry, I couldn't control your device right now. Please try again later.")

@tool
def read_document(doc_type: str, doc_id: str, context: ToolContext) -> str:
    """Read and summarize documents. Types: 'gdoc', 'pdf'."""
    try:
        if doc_type not in ('gdoc', 'pdf'):
            return make_accessible("Sorry, only Google Docs and PDFs are supported.")
        # Placeholder: Simulate document reading
        summary = "Summary: This document is about accessibility best practices. It covers clear language, structure, and screen reader support."
        return make_accessible(summary)
    except Exception:
        return make_accessible("I'm sorry, I couldn't read the document right now. Please try again later.")

@tool
def voice_command_handler(audio: bytes, context: ToolContext) -> str:
    """Process raw voice commands from microphone input."""
    try:
        # Placeholder: Simulate speech-to-text
        text = "Turn on the living room light."
        # Simulate processing the text
        return make_accessible(f"Voice command received: {text}")
    except Exception:
        return make_accessible("I'm sorry, I couldn't process your voice command right now. Please try again later.")
