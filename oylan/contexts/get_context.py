import requests
from ..config import URL_OYLAN, API_KEY, ASSISTANT_ID


HEADERS = {
    "Authorization": f"Api-Key {API_KEY}",
    "accept": "application/json"
}

def get_contexts_with_ids(assistant_id):
    url = f"{URL_OYLAN}assistant/{assistant_id}/"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        contexts = data.get("contexts", [])
        result = []
        for context in contexts:
            context_id = context.get("id")
            content = context.get("content")
            result.append((context_id, content))
        print("Contexts with IDs:")
        for ctx in result:
            print(f"ID: {ctx[0]}\nContent: {ctx[1]}\n---")
        return result
    else:
        print(f"Error retrieving contexts: {response.status_code} - {response.text}")
        return []

# use:
contexts_with_ids = get_contexts_with_ids(ASSISTANT_ID)
