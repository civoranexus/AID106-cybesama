from routing.intents import Intent
from routing.classifier import classify_intent

from services.scheme_service import (
    handle_scheme_eligibility,
    handle_scheme_info,
)
from services.llm_service import llm_fallback


def route_query(query: str, user_context: dict):
    """
    Central routing logic.
    Deterministic routes first, LLM fallback last.
    """

    intent = classify_intent(query)

    # 1️⃣ Verified scheme eligibility
    if intent == Intent.SCHEME_ELIGIBILITY:
        return handle_scheme_eligibility(query, user_context)

    # 2️⃣ Verified scheme information
    if intent == Intent.SCHEME_INFO:
        result = handle_scheme_info(query)
        if result:
            return result

    # 3️⃣ Small talk or out-of-scope → LLM
    if intent in (Intent.SMALL_TALK, Intent.OUT_OF_SCOPE):
        return llm_fallback(query)

    # 4️⃣ Safety fallback (never return nothing)
    return llm_fallback(query)
