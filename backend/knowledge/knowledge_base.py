def query_knowledge(nlu_result):
    intent = nlu_result["intent"]

    if intent == "WEATHER_QUERY":
        return {
            "answer": "आज हल्की बारिश की संभावना है"
        }

    if intent == "CROP_PRICE":
        return {
            "answer": "आज गेहूं का भाव 2200 रुपये प्रति क्विंटल है"
        }

    if intent == "SCHEME_INFO":
        return {
            "answer": "प्रधानमंत्री किसान योजना किसानों को आर्थिक सहायता देती है"
        }

    return {
        "answer": "माफ कीजिए, मैं आपकी मदद नहीं कर पाया"
    }
