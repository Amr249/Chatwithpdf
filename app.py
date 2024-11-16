import os 
from apikey import apikey 

import streamlit as st 
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

os.environ["OPENAI_API_KEY"] = apikey

st.title('meduim article generator')
topic = st.text_input('input your topic') # take the topic from the user 
# language = st.text_input('input language')  take the language from the user 


title_template = PromptTemplate(
    # this the vaariables that we will give to the model 
    input_variables = ['topic'], 
    # this is the prompt
    template = 'Give me a medium article title on {topic}'
)

article_template = PromptTemplate(
    # this the vaariables that we will give to the model 
    input_variables = ['title'], 
    # this is the prompt
    template = 'Give me a medium article for title: {title}'
)

# the llm for title generating
llm = OpenAI(temperature=0.9) 
# temperature mean creativity of the model if you want the model to be more creative icrease the temperature
title_chain = LLMChain(llm = llm , prompt = title_template)


# the llm for article generating
llm2 = ChatOpenAI(model_name ='gpt-3.5-turbo',temperature=0.9) 
article_chain = LLMChain(llm = llm2 , prompt = article_template)


overall_chain = SimpleSequentialChain(chains = [title_chain, article_chain])

if topic: 
    response = overall_chain.run(topic) # give the topic ot the llm and assign it to the response variable 
    st.write(response) # show the response in the UI