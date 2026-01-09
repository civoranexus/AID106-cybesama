def generate_alerts():
    return [
        {
            "type": "WEATHER",
            "message": "कल भारी बारिश की संभावना है",
            "priority": "HIGH"
        },
        {
            "type": "SCHEME",
            "message": "किसान योजना आवेदन की अंतिम तारीख पास है",
            "priority": "MEDIUM"
        }
    ]
