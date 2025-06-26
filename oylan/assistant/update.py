import requests
from ..config import URL_OYLAN, API_KEY

# Function to update an assistant fully or partially
def update_assistant_full(
    assistant_id,
    name,
    description,
    temperature,
    max_tokens,
    model,
    system_instructions=None,
    context=None
):
    """
    Oylan API арқылы ассистентті толық жаңарту (PUT).
    """
    url = f"{URL_OYLAN}assistant/{assistant_id}/"
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

    response = requests.put(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def update_assistant_partial(assistant_id, **kwargs):
    """
    Oylan API арқылы ассистентті жартылай жаңарту (PATCH).
    kwargs арқылы тек өзгертілетін өрістерді беріңіз.
    """
    url = f"{URL_OYLAN}assistant/{assistant_id}/"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }
    data = kwargs

    response = requests.patch(url, headers=headers, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


# update_assistant_full(
#     assistant_id=1,
#     name="AI Book Reader",
#     description="AI Assistant who reads book",
#     temperature=0.1,
#     max_tokens=500,
#     model="Oylan",
#     system_instructions="Read books and explain them",
#     context="string"
# )
update_assistant_partial(1, name="AI Book Reader 2.0")
