import requests

from ..config import URL_OYLAN, API_KEY

# Function to create a new assistant
def create_assistant(
    name,
    description,
    temperature,
    max_tokens,
    model,
    system_instructions=None,
    context=None
):
    url = f"{URL_OYLAN}assistant/"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}" 
    }
    data = {
        "name": name,
        "description": description,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "model": model
    }
    if system_instructions:
        data["system_instructions"] = system_instructions
    if context:
        data["context"] = context

    response = requests.post(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 201:
        return response.json()
    else:
        return None

create_assistant(
    name="Dake Assistant",
    description="Example Description for Assistant",
    temperature=0.5,
    max_tokens=1000,
    model="Oylan",
    system_instructions="Be nice assistant"
)