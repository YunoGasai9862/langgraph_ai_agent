from dto.state import State
from dto.message_classifier import MessageClassifier
from ..enum.message_type import MessageType

class Helper:
    
    def __init__(self, llm):
        self.llm = llm
        
    def chatbot(self, state: State):
        return {"messages": [self.llm.invoke(state["messages"])]}
    
    def router(state: State):
        message_type = state.get("message_type", MessageType.LOGICAL)
        return {"next": "therapist"} if message_type == MessageType.EMOTIONAL else {"next": "logical"}
    
    def classify_message(self, state: State):
        last_message = state["messages"][-1]
        classifier_llm = self.llm.with_structured_output(MessageClassifier)
        result = classifier_llm.invoke([
            {
                "role": "system",
                "content": """Classify the user message as either:
                - 'emotional': if it asks for emotional support, therapy, deals with feelings, or personal problems
                - 'logical': if it asks for facts, information, logical analysis, or practical solutions
                """
            },
            {
                "role": "user", "content": last_message.content
            }
        ])
        return {"message_type": result.message_type}
    
    
    def therapist_agent(self, state: State):
        pass
    
    def logical_agent(self, state: State):
        pass