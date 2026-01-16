from routing.intents import Intent

def classify_intent(query: str) -> Intent:
    q = query.lower()

    if "eligible" in q or "eligibility" in q:
        return Intent.SCHEME_ELIGIBILITY

    if "what is" in q or "tell me about" in q:
        return Intent.SCHEME_INFO

    if "document" in q:
        return Intent.DOCUMENTS_REQUIRED

    if "how to apply" in q or "apply" in q:
        return Intent.APPLICATION_PROCESS

    if q in ["hi", "hello", "hey"]:
        return Intent.SMALL_TALK

    return Intent.OUT_OF_SCOPE
