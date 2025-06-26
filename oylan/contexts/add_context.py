import requests, os
from ..config import URL_OYLAN, API_KEY, ASSISTANT_ID

# Configuration for the request headers
HEADERS = {
    "Authorization": f"Api-Key {API_KEY}",
    "accept": "application/json"
}

# Function to upload context from a DOCX file
def upload_docx_context(assistant_id, file_path):
    url = f"{URL_OYLAN}assistant/{assistant_id}/upload-docx/"

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found — {file_path}")
        return None

    try:
        with open(file_path, "rb") as docx_file:
            files = {
                "files": (os.path.basename(file_path), docx_file, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            }
            response = requests.post(url, headers=HEADERS, files=files)

        # Check the response
        if response.status_code == 200:
            print("DOCX file uploaded successfully!")
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Specify the correct path to the DOCX file
    file_path = os.path.abspath('context.docx')

    # Print the file path (for verification)
    print(f"File path: {file_path}")

    # Upload the context
    result = upload_docx_context(ASSISTANT_ID, file_path)
    if result:
        combined_context = result.get("details", {}).get("combined_context")
        if combined_context:
            print("Uploaded context:\n", combined_context)
        else:
            print("Uploaded context: Context is empty")
    else:
        print("An error occurred while uploading the context.")