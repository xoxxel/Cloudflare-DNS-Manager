import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
ZONE_ID = os.getenv('ZONE_ID')
