#  Configuration file for API settings
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_RESPONSE')
API_SOYLE = os.environ.get("API_SOYLE")
API_MAIN_SOYLE = os.environ.get("API_MAIN_SOYLE")

# Set the Assistant ID (#https://oylan.nu.edu.kz/api/v1/assistant/'ASSISTANT_ID', replace 'ASSISTANT_ID' with your actual ID )
ASSISTANT_ID = '1'  # Example: '1'

# OYLAN, Soyle App API endpoint base urls
URL_OYLAN = "https://oylan.nu.edu.kz/api/v1/"
URL_SOYLE = "https://mangisoz.nu.edu.kz/external-api/v1/"