from google.adk import Agent
from google.adk.types import ToolContext
import tools
from utils import make_accessible
import requests
from bs4 import BeautifulSoup
# Add Google Cloud features as agent tools (stubs for now)
from google.cloud import texttospeech, speech, vision, translate_v2, storage

from sub_agents.email_agent import EmailAgent
from sub_agents.calendar_agent import CalendarAgent
from sub_agents.social_agent import SocialAgent
from sub_agents.device_agent import DeviceAgent
from sub_agents.document_agent import DocumentAgent
from sub_agents.voice_agent import VoiceAgent
from sub_agents.whatsapp_business_agent import WhatsAppBusinessAgent
from sub_agents.education_agent import EducationAgent
from sub_agents.work_agent import WorkAgent
from sub_agents.business_agent import BusinessAgent
from sub_agents.hospitality_agent import HospitalityAgent
from sub_agents.learning_agent import LearningAgent
from sub_agents.earning_agent import EarningAgent
from sub_agents.health_agent import HealthAgent
from sub_agents.social_inclusion_agent import SocialInclusionAgent
from sub_agents.travel_agent import TravelAgent
from sub_agents.intent_classifier import IntentClassifier

def gather_website_data(url, analysis_type="summary"):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.get_text() for p in soup.find_all('p')]
        text = ' '.join(paragraphs)[:3000]
        if not text:
            return make_accessible("No readable content found on the page.")
        if analysis_type == "summary":
            summary = summarize_simple(text)
            return make_accessible(f"Website summary:\n{summary}")
        elif analysis_type == "keywords":
            words = text.split()
            freq = {}
            for w in words:
                freq[w] = freq.get(w, 0) + 1
            top = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
            keywords = ', '.join([w for w, _ in top])
            return make_accessible(f"Top keywords: {keywords}")
        elif analysis_type == "sentiment":
            return make_accessible("Sentiment analysis: [Stub: Neutral]")
        else:
            return make_accessible("Unknown analysis type.")
    except Exception as e:
        return make_accessible(f"Error gathering website data: {str(e)}")

# Remove in-file agent definitions, now imported from sub_agents

# Add Google Cloud feature stubs
# Text-to-Speech tool

def cloud_text_to_speech(text, lang='en-US'):
    # In production, use Google Cloud Text-to-Speech API
    return f"[Cloud TTS] Would speak: '{text}' in {lang} (stub)"

# Speech-to-Text tool

def cloud_speech_to_text(audio_path, lang='en-US'):
    # In production, use Google Cloud Speech-to-Text API
    return f"[Cloud STT] Would transcribe audio at {audio_path} (stub)"

# Vision OCR tool

def cloud_ocr_image(image_path):
    # In production, use Google Cloud Vision API
    return f"[Cloud OCR] Would extract text from {image_path} (stub)"

# Translation tool

def cloud_translate_text(text, target_lang='en'):
    # In production, use Google Cloud Translation API
    return f"[Cloud Translate] Would translate '{text}' to {target_lang} (stub)"

# BigQuery analytics tool

def cloud_bigquery_query(query):
    # In production, use Google BigQuery API
    return f"[BigQuery] Would run query: {query} (stub)"

# Add these as tools to relevant agents (example: Education, Work, Document, SocialInclusion, etc.)
EducationAgent.tools.extend([
    cloud_text_to_speech,
    cloud_translate_text
])
DocumentAgent.tools.extend([
    cloud_ocr_image,
    cloud_text_to_speech,
    cloud_translate_text
])
WorkAgent.tools.extend([
    cloud_text_to_speech,
    cloud_translate_text,
    cloud_bigquery_query
])
SocialInclusionAgent.tools.extend([
    cloud_translate_text
])
TravelAgent.tools.extend([
    cloud_translate_text
])
HealthAgent.tools.extend([
    cloud_text_to_speech
])

# Add new agents to the orchestrator
class OrchestratorAgent:
    def __init__(self):
        self.agents = {
            'email': EmailAgent,
            'calendar': CalendarAgent,
            'social': SocialAgent,
            'device': DeviceAgent,
            'document': DocumentAgent,
            'voice': VoiceAgent,
            'whatsapp_business': WhatsAppBusinessAgent,
            'education': EducationAgent,
            'work': WorkAgent,
            'business': BusinessAgent,
            'hospitality': HospitalityAgent,
            'learning': LearningAgent,
            'earning': EarningAgent,
            'health': HealthAgent,
            'social_inclusion': SocialInclusionAgent,
            'travel': TravelAgent
        }
        self.intent_classifier = IntentClassifier

    def route(self, user_input: str, context: ToolContext = None):
        try:
            intent = self.intent_classifier.run(user_input).strip().lower()
        except Exception:
            intent = 'unknown'
        if intent in self.agents:
            response = self.agents[intent].run(user_input)
        else:
            responses = [agent.run(user_input) for agent in self.agents.values()]
            response = '\n'.join([make_accessible(r) for r in responses if r])
        return make_accessible(response)

def gmail_get_emails():
    return "[Stub] Retrieved emails from Gmail API."

def gcal_get_events():
    return "[Stub] Retrieved events from Google Calendar API."

def gcs_read_document():
    return "[Stub] Read document from Google Cloud Storage."

def tts_speak(text):
    return f"[Stub] Spoke text using Cloud TTS: {text}"

def smart_home_control_device():
    return "[Stub] Controlled smart home device via Google API."

ARCHITECTURE_DIAGRAM = '''
```mermaid
graph TD
    User((User))
    Orchestrator[Orchestrator Agent\n(Gemini, LLM Intent Detection)]
    Email[EmailAgent\n(Gmail API)]
    Calendar[CalendarAgent\n(Calendar API)]
    Social[SocialAgent\n(Social Media API)]
    Device[DeviceAgent\n(Smart Home API)]
    Document[DocumentAgent\n(GCS, Docs API)]
    Voice[VoiceAgent\n(Text-to-Speech, Speech-to-Text)]
    WhatsApp[WhatsAppBusinessAgent\n(WhatsApp Business API)]
    Education[EducationAgent\n(Education API)]
    Work[WorkAgent\n(Work API)]
    Business[BusinessAgent\n(Business API)]
    Hospitality[HospitalityAgent\n(Hotel API)]
    Learning[LearningAgent\n(Course API)]
    Earning[EarningAgent\n(Job API)]
    Health[HealthAgent\n(Health API)]
    SocialInclusion[SocialInclusionAgent\n(Community API)]
    Travel[TravelAgent\n(Travel API)]

    User --> Orchestrator
    Orchestrator --> Email
    Orchestrator --> Calendar
    Orchestrator --> Social
    Orchestrator --> Device
    Orchestrator --> Document
    Orchestrator --> Voice
    Orchestrator --> WhatsApp
    Orchestrator --> Education
    Orchestrator --> Work
    Orchestrator --> Business
    Orchestrator --> Hospitality
    Orchestrator --> Learning
    Orchestrator --> Earning
    Orchestrator --> Health
    Orchestrator --> SocialInclusion
    Orchestrator --> Travel
    Email -->|API| Email
    Calendar -->|API| Calendar
    Device -->|API| Device
    Document -->|API| Document
    Voice -->|API| Voice
    WhatsApp -->|API| WhatsApp
    Education -->|API| Education
    Work -->|API| Work
    Business -->|API| Business
    Hospitality -->|API| Hospitality
    Learning -->|API| Learning
    Earning -->|API| Earning
    Health -->|API| Health
    SocialInclusion -->|API| SocialInclusion
    Travel -->|API| Travel
```
'''

README_SNIPPET = '''
# Aura: Accessibility-First Multi-Agent AI Assistant

## Overview
Aura is a multi-agent AI system built with Google ADK and Google Cloud, designed to empower people with disabilities. It orchestrates specialized agents for email, calendar, social media, smart home, documents, and voice, ensuring all outputs are accessible for screen readers and voice-first interaction.

## Architecture
- **Orchestrator Agent:** Uses Gemini LLM to classify user intent and route requests.
- **Sub-Agents:** Specialized for each domain, integrating with Google Cloud APIs.
- **Accessibility:** All responses are formatted for screen readers and voice.

## Google Cloud Integrations
- Gmail API, Calendar API, Cloud Storage, Text-to-Speech, and more.

## How to Run
1. Deploy to Google Cloud Run using Terraform (`terraform apply`).
2. Interact via the provided web or CLI interface.

## Demo Video
[YouTube Link Here]

## Architecture Diagram
{ARCHITECTURE_DIAGRAM}
'''.replace('{ARCHITECTURE_DIAGRAM}', ARCHITECTURE_DIAGRAM)

DEMO_SCRIPT = '''
1. Greet the user and explain Aura's purpose.
2. Show a voice command: "Read my latest emails."
   - Orchestrator routes to EmailAgent, which calls Gmail API (stub/demo).
3. Show a calendar request: "What are my meetings today?"
   - Routed to CalendarAgent, calls Calendar API (stub/demo).
4. Show a smart home command: "Turn on the living room lights."
   - Routed to DeviceAgent, calls Smart Home API (stub/demo).
5. Show document reading: "Read the file 'report.pdf'."
   - Routed to DocumentAgent, calls GCS (stub/demo).
6. Show accessible output (screen reader/voice) for each.
7. End with a proactive reminder from Aura (e.g., "You have an upcoming meeting in 10 minutes.")
'''

class ContextMemory:
    def __init__(self):
        self.last_intent = None
        self.last_response = None
        self.caregiver_contact = None
        self.routines = {}
    def update(self, intent, response):
        self.last_intent = intent
        self.last_response = response
    def set_caregiver(self, contact):
        self.caregiver_contact = contact
    def add_routine(self, name, actions):
        self.routines[name] = actions
    def get_routine(self, name):
        return self.routines.get(name, [])
context_memory = ContextMemory()

def proactive_notifications():
    notifications = []
    notifications.append("You have 1 urgent email from your doctor.")
    notifications.append("You have a meeting in 15 minutes.")
    notifications.append("Your front door is unlocked.")
    return '\n'.join([make_accessible(n) for n in notifications])

def morning_briefing():
    emails = gmail_get_emails()
    events = gcal_get_events()
    device = smart_home_control_device()
    return make_accessible(f"Good morning! Here’s your summary:\n{emails}\n{events}\n{device}")

def set_caregiver(contact):
    context_memory.set_caregiver(contact)
    return make_accessible(f"Caregiver contact set to {contact}.")

def notify_caregiver(message):
    if context_memory.caregiver_contact:
        return make_accessible(f"Notified caregiver ({context_memory.caregiver_contact}): {message}")
    else:
        return make_accessible("No caregiver contact set.")

def summarize_simple(text):
    return make_accessible(f"Simple summary: {text[:80]}...")

def speak_slower(text):
    return make_accessible(f"[Speaking slower] {text}")

def set_tone(tone):
    return make_accessible(f"Agent tone set to {tone}.")

def encouragement():
    return make_accessible("You're doing great! Remember to take breaks and celebrate your progress.")

class AdvancedOrchestratorAgent(OrchestratorAgent):
    def route(self, user_input: str, context: ToolContext = None):
        if user_input.strip().lower() in ["proactive", "notifications"]:
            return proactive_notifications()
        if user_input.strip().lower() == "morning briefing":
            return morning_briefing()
        if user_input.lower().startswith("set caregiver"):
            contact = user_input.split("set caregiver",1)[-1].strip()
            return set_caregiver(contact)
        if user_input.lower().startswith("notify caregiver"):
            msg = user_input.split("notify caregiver",1)[-1].strip()
            return notify_caregiver(msg)
        if user_input.lower().startswith("summarize simple"):
            text = user_input.split("summarize simple",1)[-1].strip()
            return summarize_simple(text)
        if user_input.lower().startswith("speak slower"):
            text = user_input.split("speak slower",1)[-1].strip()
            return speak_slower(text)
        if user_input.lower().startswith("set tone"):
            tone = user_input.split("set tone",1)[-1].strip()
            return set_tone(tone)
        if user_input.strip().lower() in ["encourage me", "motivate me"]:
            return encouragement()
        if user_input.lower().startswith("gather website data"):
            parts = user_input.split()
            url = None
            analysis_type = "summary"
            for i, part in enumerate(parts):
                if part.startswith("http"):
                    url = part
                if part in ["summary", "keywords", "sentiment"]:
                    analysis_type = part
            if not url:
                return make_accessible("Please provide a website URL. Example: 'Gather website data https://news.ycombinator.com summary'")
            return make_accessible(f"Do you want me to visit {url} and perform {analysis_type} analysis? Reply 'yes' to confirm.")
        if user_input.lower().startswith("yes") and context_memory.last_intent == "gather_website_data":
            url = context_memory.last_response.split()[3]
            analysis_type = context_memory.last_response.split()[-1]
            result = gather_website_data(url, analysis_type)
            return make_accessible(f"Here are the main points from {url}:\n{result}")
        try:
            intent = self.intent_classifier.run(user_input).strip().lower()
        except Exception:
            intent = 'unknown'
        action_required = False
        action_message = ""
        if intent == 'social' and any(x in user_input.lower() for x in ['post', 'facebook', 'whatsapp', 'business']):
            action_required = True
            action_message = "Do you want me to post this on your social media (Facebook, WhatsApp Business)? Please reply 'yes' to confirm."
        if action_required:
            context_memory.update(intent, user_input)
            return make_accessible(f"Before I proceed:\n- {action_message}")
        if intent in self.agents:
            response = self.agents[intent].run(user_input)
        else:
            responses = [agent.run(user_input) for agent in self.agents.values()]
            response = '\n'.join([make_accessible(r) for r in responses if r])
        context_memory.update(intent, response)
        if intent == 'calendar' and 'meeting' in user_input.lower():
            response += '\nWould you like to email the attendees? Say: "Email attendees about [subject]".'
        points = [f"- {line.strip()}" for line in response.split('\n') if line.strip()]
        return make_accessible("Here are the main points:\n" + '\n'.join(points))

orchestrator = AdvancedOrchestratorAgent()

if __name__ == "__main__":
    print("\n--- SAMPLE README SECTION ---\n")
    print(README_SNIPPET)
    print("\n--- DEMO SCRIPT OUTLINE ---\n")
    print(DEMO_SCRIPT)
    print("\n--- ARCHITECTURE DIAGRAM (Mermaid) ---\n")
    print(ARCHITECTURE_DIAGRAM)
    print("\nWelcome to Aura, your accessibility-first multi-agent assistant!")
    print("Type your request (or 'exit' to quit):")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == 'exit':
            print("Goodbye!")
            break
        output = orchestrator.route(user_input)
        print(f"Aura: {output}")
