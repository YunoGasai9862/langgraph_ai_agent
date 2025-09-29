from typing import Literal
from pydantic import BaseModel, Field
from ..enum.message_type import MessageType

class MessageClassifier(BaseModel):
    message_type: MessageType = Field(
        ...,
        description="Classify if the message requires and emotional (therapist) or logical response"
    )