from typing import Optional
from .base import BaseResponse

class ErrorResponse(BaseResponse):
    error_code: str
    resolution_hint: Optional[str] = None
