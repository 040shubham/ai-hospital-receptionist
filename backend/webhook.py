import requests
from datetime import datetime

RELAY_WEBHOOK_URL = "https://hook.relay.app/api/v1/playbook/cmk9todkq5w4k0qm47ui63zta/trigger/LT1w3WRnSN0FOZQso_5zbw"

def send_webhook(state):
    payload = {
        "patient_name": state["name"],
        "patient_age": state["age"],
        "patient_query": state["query"],
        "ward": state["ward"],
        "timestamp": datetime.utcnow().isoformat()
    }

    requests.post("https://hook.relay.app/api/v1/playbook/cmk9todkq5w4k0qm47ui63zta/trigger/LT1w3WRnSN0FOZQso_5zbw", json=payload)
