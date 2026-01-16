from pydantic import BaseModel
from typing import Literal

class BaseResponse(BaseModel):
    success: bool
    message: str
    source: Literal["database", "llm", "hybrid"]
