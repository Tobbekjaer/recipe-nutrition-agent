import json
import os
from datetime import datetime

LOG_FILE = "tool_calls.log"

def log_tool_call(tool_name: str, inputs: dict, output: dict) -> None:
    """
    Logs every tool call with timestamp, inputs, and output.
    Appends to tool_calls.log so the full session history is preserved.
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "tool": tool_name,
        "inputs": inputs,
        "output": output,
    }

    # Append to log file - "a" means we never overwrite previous entries
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")