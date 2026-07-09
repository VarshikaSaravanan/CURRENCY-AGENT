import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    """
    Load previous conversation history.
    """
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    return []

def save_memory(messages):
    """
    Save conversation history.
    """
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2)