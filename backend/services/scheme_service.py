from database.schemas.scheme import SchemeResponse, EligibilityCheck
from services.llm_service import explain_scheme_with_llm


def handle_scheme_eligibility(query: str, user_context: dict) -> SchemeResponse:
    # Example: PM Awas Yojana (hardcoded for now)
    checks = [
        EligibilityCheck(
            condition="Annual income below ₹3,00,000",
            satisfied=user_context.get("income", 0) < 300000
        ),
        EligibilityCheck(
            condition="Does not own a pucca house",
            satisfied=not user_context.get("owns_house", False)
        )
    ]

    eligible = all(check.satisfied for check in checks)

    response = SchemeResponse(
        success=True,
        message="Eligibility evaluated",
        source="hybrid",
        scheme_name="PM Awas Yojana",
        eligible=eligible,
        eligibility_checks=checks,
        benefits=[
            "Financial assistance up to ₹1.2 lakh"
        ],
        next_steps=["Visit nearest CSC center"] if eligible else None
    )

    # 🔑 STEP 9: Grounded LLM explanation (SAFE)
    response.explanation = explain_scheme_with_llm(response)

    return response


def handle_scheme_info(query: str):
    # Placeholder — will be replaced by DB-backed InfoResponse
    return None
