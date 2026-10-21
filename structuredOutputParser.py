from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

# 1. Define the structure using Pydantic
class FactSchema(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")

# 2. Bind the schema directly to the model
model = ChatOpenAI().with_structured_output(FactSchema)

# 3. Create a clean prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a knowledgeable assistant."),
    ("human", "Give 3 facts about {topic}")
])

# 4. Build the chain
chain = prompt | model

# 5. Invoke and print the result
result = dict(chain.invoke({"topic": "black hole"}))

print(result)
# Access individual facts directly:
print(result['fact_1'])