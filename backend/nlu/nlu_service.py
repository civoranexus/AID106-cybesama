from langdetect import detect
import spacy

# Load models once
nlp_en = spacy.load("en_core_web_sm")
nlp_multi = spacy.load("xx_ent_wiki_sm")

INTENT_KEYWORDS = {
    "WEATHER_QUERY": ["weather", "rain", "मौसम", "बारिश"],
    "CROP_PRICE": ["price", "भाव", "rate", "दाम"],
    "SCHEME_INFO": ["scheme", "योजना", "pm kisan", "किसान"]
}

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return "unknown"

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def classify_intent(text):
    text = text.lower()

    INTENT_PATTERNS = {
        "WEATHER_QUERY": ["मौसम", "मुसम", "weather", "rain", "barish", "बारिश"],
        "CROP_PRICE": ["भाव", "दाम", "price", "rate"],
        "SCHEME_INFO": ["योजना", "scheme", "kisan", "किसान"]
    }

    for intent, keywords in INTENT_PATTERNS.items():
        for kw in keywords:
            if kw in text:
                return intent

            # fuzzy match for ASR errors
            for word in text.split():
                if similar(word, kw) > 0.7:
                    return intent

    return "UNKNOWN"


def extract_entities(text, lang):
    if lang == "en":
        doc = nlp_en(text)
    else:
        doc = nlp_multi(text)

    entities = {}
    for ent in doc.ents:
        entities[ent.label_] = ent.text

    return entities

def process_text(text, user_language=None):
    detected_lang = detect_language(text)

    intent = classify_intent(text)
    entities = extract_entities(text, detected_lang)

    confidence = 0.9 if intent != "UNKNOWN" else 0.5

    return {
        "text": text,
        "language": detected_lang,
        "intent": intent,
        "entities": entities,
        "confidence": confidence
    }

if __name__ == "__main__":
    tests = [
        "आज मौसम कैसा रहेगा",
        "गेहूं का भाव क्या है",
        "What is the weather today",
        "PM Kisan scheme details"
    ]

    for t in tests:
        print(process_text(t))