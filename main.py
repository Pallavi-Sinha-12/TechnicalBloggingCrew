import os
from dotenv import load_dotenv
import agentops

load_dotenv()


from src.bloggging_multi_agent_crew.crew import BloggingCrew

def run():
    # inputs = {"topic_details" : "Explain basics of FastAPI framework."}
    inputs = {"topic_details" : "Explain Python decorators."}

    agentops.init()
    BloggingCrew().blogging_crew().kickoff(inputs = inputs)

if __name__ == "__main__":
    run()