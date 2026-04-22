from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict
 
load_dotenv()
# Add the rest

class State(TypedDict):
    # update add_messages to append messages, not overwrite
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)           # 1. Declare the shape
graph_builder.add_node("chat_agent", chat_agent)  # 2. Add the node
graph_builder.set_entry_point("chat_agent")       # 3. Where to start
graph_builder.set_finish_point("chat_agent")      # 4. Where it's safe to exit
self.chain = graph_builder.compile(checkpointer=memory)  # 5. Compile

def chat_agent(state: State):
    return {"messages": [sp_function.invoke(state["messages"])]}

system_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert advisor at Yenbase ... "),
    ("placeholder", "{messages}"),
    ("human", "{input}"),
])
 
sp_function = system_prompt | model   # pipe: prompt formats, then model runs
