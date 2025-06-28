# main.py

from fastapi import FastAPI, Request
from agent import AdvancedOrchestratorAgent
from google.adk.types import ToolContext

print("🌟 Starting Aura FastAPI agent... inside Cloud Run.")

app = FastAPI()
orchestrator = AdvancedOrchestratorAgent()

@app.get("/")
def health_check():
    return {"message": "Aura is live!"}

@app.post("/query")
async def query_handler(req: Request):
    body = await req.json()
    user_input = body.get("input", "")
    response = orchestrator.route(user_input, context=ToolContext())
    return {"response": response}
