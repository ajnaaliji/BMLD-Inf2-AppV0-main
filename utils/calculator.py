from datetime import datetime

def calculate_calories(age, weight, height, gender, activity_level):
    """Berechnet den täglichen Kalorienbedarf basierend auf dem BMR + Aktivitätslevel."""
    
    if gender == "Männlich":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height * 100) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height * 100) - (4.3 * age)

    activity_factors = {
        "Gering": 1.2,
        "Leicht aktiv": 1.375,
        "Moderat aktiv": 1.55,
        "Sehr aktiv": 1.725,
        "Extrem aktiv": 1.9
    }

    daily_calories = bmr * activity_factors[activity_level]

    return {"calories": round(daily_calories), "timestamp": datetime.now()}
