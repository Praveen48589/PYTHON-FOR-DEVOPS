from asyncio import tools

from strands import Agent
from strands_tools import file_read
from strands.models.ollama import OllamaModel


SYSTEM_PROMPT = """
YOU ARE A LOG ANALYSIS AGENT.

YOU ARE EXCELLENT IN READING AND UNDERSTANDING THE LOG FILES i.e (.log).
you can deduce  results in short and crisp manner
you are helpful and use a Devops mindset in Log Analysis and Root Causes
"""

ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.1"               # Specify which model to use
)

agent  = Agent(system_prompt=SYSTEM_PROMPT,
    model = ollama_model, #Calling Ollama Model
    tools=[file_read])    

agent("Detect how many time INFO , WARNING , ERROR occurs in app.log file and return the counts of them")