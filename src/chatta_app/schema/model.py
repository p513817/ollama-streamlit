from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class Details(BaseModel):
    parent_model: str = Field(..., alias="parent_model")
    format: str = Field(..., alias="format")
    family: str = Field(..., alias="family")
    families: List[str] = Field(..., alias="families")
    parameter_size: str = Field(..., alias="parameter_size")
    quantization_level: str = Field(..., alias="quantization_level")


class Model(BaseModel):
    name: str = Field(..., alias="name")
    model: str = Field(..., alias="model")
    modified_at: datetime = Field(..., alias="modified_at")
    size: int = Field(..., alias="size")
    digest: str = Field(..., alias="digest")
    details: Details = Field(..., alias="details")


class OllamaResponse(BaseModel):
    models: List[Model] = Field(..., alias="models")
