from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model


model = ChatOpenAI()

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me name of a fictional character\n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# chain = template | model | parser

chain = template | model 


result = chain.invoke({})

print(result)
