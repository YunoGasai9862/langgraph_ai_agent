from dto.state import State

class Helper:
    
    def __init__(self, llm):
        self.llm = llm
        
    def chatbot(self, state: State):
        return {"messages": [self.llm.invoke(state["messages"])]}