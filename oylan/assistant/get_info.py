import requests

from ..config import URL_OYLAN, API_KEY 

# Function to check for existing assistants or create a new one
def check_or_create_assistant():
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json"
    }

    # Fetch existing assistants
    url= f"{URL_OYLAN}assistant"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        assistants = response.json()
        if assistants:
            # assistant_ids = [assistant["id"] for assistant in assistants]
            assistant_id = assistants[0]["id"]
            return assistant_id
        else:
            # Create a new assistant if none exist
            pass
    else:
        # Print error status if unable to fetch assistants
        print(f"Error fetching assistants: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

def get_assistant_name_by_id(assistant_id):
    headers = {
        "Authorization": f"Api-Key {API_KEY}",
        "accept": "application/json"
    }
    url = f"{URL_OYLAN}assistant"  # Барлық ассистенттер тізімі
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        assistants = response.json()
        for assistant in assistants:
            if str(assistant.get("id")) == str(assistant_id):
                # print(f"Assistant found with ID: {assistant_id}, name: {assistant.get('name')}")
                return assistant.get("name")
        print(f"Assistant with ID {assistant_id} not found.")
        return None
    else:
        print(f"Error fetching assistants: {response.status_code}")
        print(f"Response content: {response.text}")
        return None

if __name__ == "__main__":
    response = check_or_create_assistant()
    if response:
        assistant_name = get_assistant_name_by_id(response)
        print(f"ASSISTANT NAME: {assistant_name}")
    else:
        print("No assistant found or created.")
    print(f"ASSISTANT ID's: {response}")