from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from cultural_heritage.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool

@CrewBase
class CulturalHeritage():
	"""CulturalHeritage crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def cultural_heritage_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['cultural_heritage_researcher'],
			tools=[SerperDevTool()], #MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def cultural_heritage_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['cultural_heritage_writer'],
			tools=[SerperDevTool()],
			#llm="groq/deepseek-r1-distill-llama-70b",#llama-3.3-70b-versatile",
			verbose=True
		)

	@task
	def heritage_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['heritage_research_task'],
		)

	@task
	def heritage_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['heritage_writing_task'],
			#output_file='report.md'
		)
  
	@task
	def heritage_research_task_1(self) -> Task:
		return Task(
			config=self.tasks_config['heritage_research_task_1'],
			#output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CulturalHeritage crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
