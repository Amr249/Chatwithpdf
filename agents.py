'''
- the code in this file is not working i dont know why? even chatgpt couldnt solve the problem 
- what i understood from the video that agents are used to search the web for informations and deal with 
complex math problems because llms cant perform well
on those tasks.

- make a further reasearch on AI agents.

'''


import os 
from apikey import apikey 

from langchain_community.llms import OpenAI
from langchain_community.agent_toolkits import load_tools
from langchain.agents import AgentType, initialize_agent

os.environ["OPENAI_API_KEY"] = apikey


# Instantiate the OpenAI language model
llm = OpenAI(temperature=0.0)

# Load tools and initialize the agent
tools = load_tools(['wikipedia', 'llm-math'], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
prompt = input('wikipedia research task')

agent.run(prompt)