# langchain_message.py
from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

load_dotenv()
model = init_chat_model("google_genai:gemini-2.5-flash",  temperature=0.2)

response = model.invoke([HumanMessage(content="Hello, my name is Max! What is your favorite Python library?")])
print(response)

response = model.invoke([HumanMessage(content="What is my name")])
print(response)
