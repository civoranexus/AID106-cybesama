def process_text(text, language):
    """
    Basic intent detection (rule-based for now)
    """

    text_lower = text.lower()

    if "मौसम" in text_lower or "weather" in text_lower:
        intent = "WEATHER_QUERY"
    elif "भाव" in text_lower or "price" in text_lower:
        intent = "CROP_PRICE"
    elif "योजना" in text_lower or "scheme" in text_lower:
        intent = "SCHEME_INFO"
    else:
        intent = "UNKNOWN"

    return {
        "intent": intent,
        "entities": {},
        "confidence": 0.8
    }
