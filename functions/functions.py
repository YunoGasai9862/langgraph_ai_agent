from dto.state import State

def chatbot(llm, state: State):
    return {"messages": [llm.invoke(state["messages"])]}