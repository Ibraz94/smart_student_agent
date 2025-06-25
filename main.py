from dotenv import load_dotenv
from agents import Agent, Runner

load_dotenv()


agent = Agent(
    name = "Student Assistant",
    instructions = "You are a student assistant. You are responsible for answer academic questions, provide study tips and summerize small text passages.",
    )

result = Runner.run_sync(agent, "What is the capital of Pakistan?")

print(result.final_output)
