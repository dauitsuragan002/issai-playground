import requests

from config import *

def get_available_models():
    url = f"{URL_OYLAN}assistant/models/"
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        response_data = response.json()
        # Әрбір dict үшін барлық кілттерді шығару
        for item in response_data:
            print("id:", item.get("id"))
            print("name:", item.get("name"))
            print("description:", item.get("description"))
            print("max_tokens:", item.get("max_tokens"))
            print("training_data:", item.get("training_data"))
            print("default_temperature:", item.get("default_temperature"))
            print("is_active:", item.get("is_active"))
            print("---")
        return response_data
    else:
        return None

# Мысал қолдану:
get_available_models()