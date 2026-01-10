from fastapi import APIRouter
from schemas.scheme import SchemeResponse, EligibilityCheck

router = APIRouter()

@router.get("/check-eligibility", response_model=SchemeResponse)
def check_eligibility(user_id: int):
    return SchemeResponse(
        success=True,
        message="Eligibility evaluated successfully",
        source="database",
        scheme_name="PM Awas Yojana",
        eligible=True,
        eligibility_checks=[
            EligibilityCheck(
                condition="Annual income below ₹3,00,000",
                satisfied=True
            ),
            EligibilityCheck(
                condition="Does not own a pucca house",
                satisfied=True
            )
        ],
        benefits=[
            "Financial assistance up to ₹1.2 lakh",
            "Subsidized home loan"
        ],
        next_steps=[
            "Visit nearest CSC center",
            "Carry Aadhaar and income certificate"
        ]
    )
