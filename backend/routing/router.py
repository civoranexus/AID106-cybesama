from routing.intents import Intent
from routing.classifier import classify_intent
from services.scheme_service import (
    handle_scheme_eligibility,
    handle_scheme_info,
)
from services.llm_service import handle_llm_fallback

def route_query(query: str, user_context: dict):
    intent = classify_intent(query)

    if intent == Intent.SCHEME_ELIGIBILITY:
        return handle_scheme_eligibility(query, user_context)

    if intent == Intent.SCHEME_INFO:
        return handle_scheme_info(query)

    if intent in [Intent.SMALL_TALK, Intent.OUT_OF_SCOPE]:
        return handle_llm_fallback(query)

    return handle_llm_fallback(query)
