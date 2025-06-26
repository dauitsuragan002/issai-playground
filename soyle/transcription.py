import requests

from config import  URL_SOYLE, API_SOYLE

# Function to recognize speech
def recognize_speech(user_id, audio_file_path):

    url = f"{URL_SOYLE}transcript/transcript_audio/"

    headers = {
        "Authorization": f"Bearer {API_SOYLE}"
    }

    # Send the file as multipart/form-data
    with open(audio_file_path, "rb") as f:
        files = {"file": (audio_file_path, f, "audio/wav")}
        response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        result = response.json()
        print(result.get("transcription_text"))
        return result.get("transcription_text")
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return f"Error: {response.status_code}, {response.text}"
    
recognize_speech("user_id", "input_audio.wav.wav")