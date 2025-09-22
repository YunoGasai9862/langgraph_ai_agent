from typing import Literal
from pydantic import BaseModel, Field

class MessageClassifier(BaseModel):
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires and emotional (therapist) or logical response"
    )