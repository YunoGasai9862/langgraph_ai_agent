from typing import List
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from ..enum.message_type import MessageType

class State(TypedDict):
    messages: Annotated[List, add_messages]
    message_type: MessageType | None