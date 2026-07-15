import requests

API_KEY = "c37b756017f13fb22cad41b1c995fff2"

url = f"https://api.aviationstack.com/v1/flights?access_key={API_KEY}"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(data)