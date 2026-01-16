from pydantic import BaseModel
from typing import List, Optional
from .base import BaseResponse


class EligibilityCheck(BaseModel):
    condition: str
    satisfied: bool


class SchemeResponse(BaseResponse):
    scheme_name: str
    eligible: bool
    eligibility_checks: List[EligibilityCheck]
    benefits: List[str]
    next_steps: Optional[List[str]] = None

    # 🔑 ADD THIS LINE
    explanation: Optional[str] = None
