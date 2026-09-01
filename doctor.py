from  langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv
from pydantic import BaseModel,Field
import os 
import streamlit as st
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
llm = ChatOpenRouter(
    model="gpt-oss-20b",
    openrouter_api_key=os.getenv("OPENROUTER_API_KEY")

)
from typing import List

class Doctor(BaseModel):
    questions: str = Field(description="ask question for clarification")
    disease: str = Field(description="disease of patient")
    precautions: List[str] = Field(description="precautions")
    tablets: List[str] = Field(description="OTC medicines if appropriate")
    signs: List[str] = Field(description="danger signs")
parcer = PydanticOutputParser(
    pydantic_object=Doctor
)

prompt = ChatPromptTemplate.from_messages([
    

("system","""
You are a medical information assistant.

Use the entire conversation history before answering.

If the user has already answered previous questions,
combine those answers with earlier symptoms.

Do not forget information mentioned earlier in the chat.

If information is insufficient:

- Ask only the most important missing question.
- disease = "Need More Information"

Never ignore conversation history.

{format_instructions}

"""),
MessagesPlaceholder(variable_name="history"),
("human","{input}")]
)

chain = prompt.partial(
    format_instructions = parcer.get_format_instructions()
)|llm|parcer


if "store" not in st.session_state:
    st.session_state.store = {}

def get_history(session_id:str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id]=InMemoryChatMessageHistory()
    return st.session_state.store[session_id]


mentor = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history"

)
st.set_page_config(
    page_title="DOCTOR",
    page_icon="🩺"
)

st.title("🩺HEALTH SPECIALIST")
st.write("what is your health isssue")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["context"])

user_input = st.chat_input("are you fine ? ")

if user_input:
    st.session_state.messages.append(
        {"role":"user","context":user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("responding..........."):

        try:
            response=mentor.invoke(
            {"input":user_input },
            config={
                "configurable":{
                    "session_id":"sandeep"
                }
            }


        )

        except Exception as e:
          
             st.error(f"Error: {e}")
             st.stop()
        answer = f"""

{response.questions}       
### Disease
{response.disease}

### Precautions
{response.precautions}

### Tablets
{response.tablets}

### Danger Signs
{response.signs}
"""
        st.session_state.messages.append(
            {"role":"assistant","context":answer}

        )
        
        with st.chat_message("assistant"):
          st.markdown(answer)
        
        


