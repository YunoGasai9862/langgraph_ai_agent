from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dto.state import State
from functions.functions import chatbot
import os

load_dotenv(verbose=True)

llm = init_chat_model(
    model="gpt-4o", api_key = os.environ["OPEN_AI_API_KEY"], model_provider="openai",  temperature=0
)

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

user_input = input("Enter your message: ")
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})

print(state["messages"])