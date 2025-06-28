# Aura AI Agent Architecture

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

---

**Key Points:**
- The Orchestrator Agent uses Gemini LLM for intent detection and routes requests to specialized sub-agents.
- Each sub-agent integrates with relevant Google Cloud APIs or external services.
- All outputs are formatted for accessibility (screen readers, voice, etc.).
- Proactive notifications, routines, and permission checks are built-in.

See instructions/INSTRUCTIONS.md for agent roles and philosophy.
