from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool
from .custom_tools.save_blog import save_blog
from .custom_tools.publish_blog import publish_blog
from .callbacks.intermediate_logging import intermidate_logging

@CrewBase
class BloggingCrew():

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-4-turbo")

    @agent
    def researcher_agent(self) -> Agent:
        search_tool = SerperDevTool()
        return Agent(
            tools = [search_tool],
            config = self.agents_config['researcher_agent'],
            llm = self.llm,
            step_callback = lambda response: intermidate_logging(response, 'researcher_agent', 'logs/researcher_agent.log')
        )
    
    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            tools = [save_blog],
            config = self.agents_config['writer_agent'],
            llm = self.llm,
            step_callback = lambda response: intermidate_logging(response, 'writer_agent', 'logs/writer_agent.log')
        )
    
    @agent
    def publisher_agent(self) -> Agent:
        return Agent(
            tools = [publish_blog],
            config = self.agents_config['publisher_agent'],
            llm = self.llm,
            step_callback = lambda response: intermidate_logging(response, 'publisher_agent', 'logs/publisher_agent.log')
        )
    
    @task
    def research_content(self) -> Task:
        return Task(
            config = self.tasks_config['research_content'],
            agent = self.researcher_agent()
        )
    
    @task
    def write_content(self) -> Task:
        return Task(
            config = self.tasks_config['write_blog'],
            agent = self.writer_agent()
        )
    
    @task
    def publish_content(self) -> Task:
        return Task(
            config = self.tasks_config['publish_blog'],
            agent = self.publisher_agent()
        )
    
    @crew
    def blogging_crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose=2
        )