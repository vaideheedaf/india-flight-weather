import requests
import pandas as pd

def extract_flights():
    print("Extracting flight data...")

    api_key = "bb273e74b6c56441e21a237c2c69bb3e"

    url = "https://api.aviationstack.com/v1/flights"

    params = {
        "access_key": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("✅ Flight data extracted")

        data = response.json()

        print(data)

    else:
        raise Exception(f"Flight API failed: {response.status_code}")

extract_flights()
 