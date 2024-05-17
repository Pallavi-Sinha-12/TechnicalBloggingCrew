from langchain_core.agents import AgentFinish
import json
from typing import Union, List, Tuple, Dict
from langchain.schema import AgentFinish
from datetime import datetime
import os

def intermidate_logging(agent_output: Union[str, List[Tuple[Dict, str]], AgentFinish], agent_name, log_file_path: str):
    os.makedirs("logs", exist_ok=True)
    current_time = datetime.utcnow().isoformat().format("YYYY-MM-DD HH:mm:ss")
    print(f"Current time: {current_time}")
    if isinstance(agent_output, list) and all(isinstance(item, tuple) for item in agent_output):
        for action, description in agent_output:
            print("Agent intermediate log:")
            agent_log = f"Agent: {agent_name},\n Tool: {getattr(action, 'tool', 'Unknown')},\n Tool Input: {getattr(action, 'tool_input', 'Unknown')}, \n Log: {getattr(action, 'log', 'Unknown')}, \n Timestamp: {current_time}"
            with open(log_file_path, 'a') as log_file:
                log_file.write(agent_log)
                log_file.write("\n\n\n")
    elif isinstance(agent_output, AgentFinish):
        print("Agent finished.")
        agent_log = f"Agent: {agent_name},\n Tool: {getattr(agent_output, 'tool', 'Unknown')},\n Tool Input: {getattr(agent_output, 'tool_input', 'Unknown')}, \n Log: {getattr(agent_output, 'log', 'Unknown')}, \n Timestamp: {current_time}"
        with open(log_file_path, 'a') as log_file:
            log_file.write(json.dumps(agent_log))
            log_file.write("\n\n\n")
