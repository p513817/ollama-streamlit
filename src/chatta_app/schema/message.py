from typing import List

from pydantic import BaseModel, Field


class OllamaMessage(BaseModel):
    role: str = Field(..., alias="role")
    content: str = Field(..., alias="content")


class OllamaRequestData(BaseModel):
    model: str = Field(..., alias="model")
    messages: List[OllamaMessage] = Field(..., alias="messages")
