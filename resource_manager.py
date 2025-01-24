import requests
from airtable_config import AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME

BASE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
HEADERS = {"Authorization": f"Bearer {AIRTABLE_API_KEY}"}

def fetch_resources():
    """Fetch all resources from Airtable."""
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        return response.json()["records"]
    else:
        print("Error fetching data:", response.status_code)
        return None