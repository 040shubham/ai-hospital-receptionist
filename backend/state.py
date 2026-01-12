# state.py

sessions = {}

def get_state(session_id: str):

    if session_id not in sessions:
        sessions[session_id] = {
            "name": None,
            "age": None,
            "query": None,
            "ward": None,
            "completed": False
        }

    return sessions[session_id]
