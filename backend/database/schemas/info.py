from typing import Optional
from .base import BaseResponse

class InfoResponse(BaseResponse):
    title: str
    summary: str
    details: Optional[str] = None
