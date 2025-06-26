import requests
from ..config import URL_OYLAN, API_KEY, ASSISTANT_ID

def delete_context(assistant_id, context_id):
    """
    Oylan API арқылы ассистенттің контекст файлын жою.
    :param assistant_id: ассистент ID
    :param context_id: контекст ID
    :return: True (жойылды) немесе False (қате)
    """
    url = f"{URL_OYLAN}assistant/{assistant_id}/contexts/{context_id}/"
    headers = {
        "accept": "application/json",
        "Authorization": f"Api-Key {API_KEY}"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"{context_id} - context deleted successfully.")
        return True
    else:
        print(f"Error deleting context: {response.status_code}")
        print(f"Response: {response.text}")
        return False

# Example usage:
delete_context(ASSISTANT_ID, 'context_id')
