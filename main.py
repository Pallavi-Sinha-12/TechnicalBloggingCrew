from dotenv import load_dotenv
import agentops
from src.bloggging_multi_agent_crew.crew import BloggingCrew

load_dotenv()

def run():
    # inputs = {"topic_details" : "Explain basics of FastAPI framework."} # Topic 1
    inputs = {"topic_details" : "Explain Python decorators."} # Topic 2
    agentops.init()
    BloggingCrew().blogging_crew().kickoff(inputs = inputs)

if __name__ == "__main__":
    run()