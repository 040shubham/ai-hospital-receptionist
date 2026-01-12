from graph_state import PatientState

#Router Node (Ward decide karna)

def router_node(state: PatientState):
    text = state["query"] or ""
    text = text.lower()

    if "accident" in text or "pain" in text:
        return {"ward": "Emergency"}
    elif "stress" in text or "depression" in text:
        return {"ward": "Mental Health"}
    return {"ward": "General"}

#Name Node (Naam puchhna)

def name_node(state: PatientState):
    if not state.get("name"):
        return {"message": "May I know your name?"}
    return {}

#Age Node (Age puchhna)

def age_node(state: PatientState):
    if not state.get("age"):
        return {"message": "Please tell your age."}
    return {}

#Query Node (Problem puchhna)

def query_node(state: PatientState):
    if not state.get("query"):
        return {"message": "Please describe your health issue."}
    return {}




from db import supabase
from webhook import send_webhook

def save_node(state):
    if state.get("completed"):
        return {}

    if state.get("name") and state.get("age") and state.get("query") and state.get("ward"):
        supabase.table("patients").insert({
            "name": state["name"],
            "age": state["age"],
            "query": state["query"],
            "ward": state["ward"]
        }).execute()

        send_webhook(state)

        return {
            "completed": True,
            "message": "Thank you. Your details have been registered successfully."
        }

    return {}
