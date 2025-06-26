import logging
import requests
import base64
import json

from config import *

# Function to synthesize speech
def synthesize_speech(text, output_file, language):
    try:
        # URL for the Soyle API
        url = f"{URL_SOYLE}translate/text/?output_format=audio&output_voice=female"

        # Parameters for the API request
        data = {
            "source_language": language,
            "target_language": language,
            "text": text,
        }

        HEADERS = {
            "Authorization": f"Api-Key {API_SOYLE}",
            "Content-Type": "application/json"
        }

        # Send request to Soyle API
        response = requests.post(url, headers=HEADERS, json=data)

        # Check response status
        if response.status_code == 200:
            response_data = response.json()
            audio_hex = response_data.get("audio")

            if audio_hex:
                # Convert hex to Base64 and decode to audio file
                audio_base64 = hex_to_base64(audio_hex)
                audio_data = base64.b64decode(audio_base64)

                # Write audio data directly to BytesIO
                output_file.write(audio_data)
                output_file.seek(0)  # Move pointer to the start of the file

                logging.info("Audio successfully generated and written to BytesIO.")
            else:
                logging.error("Error: No audio content received.")
        else:
            logging.error(f"API error: {response.status_code} - {response.text}")

    except Exception as e:
        logging.error(f"An error occurred during speech synthesis: {e}")

# Function to convert hex string to Base64
def hex_to_base64(hex_string: str) -> str:
    """
    Convert a hex string to Base64.
    """
    byte_data = bytes.fromhex(hex_string)
    base64_data = base64.b64encode(byte_data)
    return base64_data.decode('utf-8')

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    text = "Біздің Дәке керемет, одан асқан не керек?"
    language = "kaz"
    
    # Use BytesIO to handle audio data in memory
    from io import BytesIO
    output_file = BytesIO()

    synthesize_speech(text, output_file, language)

    # Save the audio to a file for testing purposes
    with open("output_audio.mp3", "wb") as f:
        f.write(output_file.getvalue())
    output_file.close()
    logging.info("Audio saved to output_audio.mp3")
    logging.info("Program completed successfully.")