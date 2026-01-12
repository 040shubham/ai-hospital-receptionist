from dotenv import load_dotenv
import os

load_dotenv()


from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client
from state import get_state
from webhook import send_webhook

# -----------------------------
# FASTAPI APP
# -----------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # frontend allow
    allow_methods=["*"],   # POST, OPTIONS, GET sab
    allow_headers=["*"],
)

# -----------------------------
# SUPABASE CONFIG
# -----------------------------
SUPABASE_URL = os.getenv("SUPABASE_URL")

SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -----------------------------
# WARD CLASSIFICATION
# -----------------------------
def classify_ward(text: str):
    text = text.lower()
    if "accident" in text or "pain" in text or "emergency" in text:
        return "Emergency"
    elif "stress" in text or "depression" in text:
        return "Mental Health"
    else:
        return "General"

# -----------------------------
# REQUEST MODEL
# -----------------------------
class ChatRequest(BaseModel):
    message: str
    session_id: str

# -----------------------------
# CHAT API (AI RECEPTIONIST)
# -----------------------------
@app.post("/chat")
def chat(req: ChatRequest):

    state = get_state(req.session_id)
    msg = req.message

    # 1️⃣ Ward decide (once)
    if not state["ward"]:
        state["ward"] = classify_ward(msg)

    # 2️⃣ Name
    if not state["name"]:
        state["name"] = msg
        return {"reply": "Thank you. Please tell your age."}

    # 3️⃣ Age
    if not state["age"]:
        if msg.isdigit():
            state["age"] = int(msg)
            return {"reply": "Please describe your health problem."}
        else:
            return {"reply": "Please enter age in numbers only."}

    # 4️⃣ Problem
    if not state["query"]:
        state["query"] = msg

        print("Saving to Supabase:", state)

        # Save to Supabase
        supabase.table("patients").insert({
            "name": state["name"],
            "age": state["age"],
            "query": state["query"],
            "ward": state["ward"]
        }).execute()

        # Send webhook
        send_webhook(state)

        state["completed"] = True

        return {
            "reply": "Thank you. Doctor will attend you shortly.",
            "ward": state["ward"]
        }

    return {"reply": "Your request is already completed."}
