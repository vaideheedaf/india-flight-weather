import requests

API_KEY = "c37b756017f13fb22cad41b1c995fff2"

url = "https://api.aviationstack.com/v1/flights"
params= {
    "access_key": API_KEY,
  "dep_iata":"DEL"
}

response = requests.get(url, params=params)

print("Status:", response.status_code)
print("URL Sent:", response.url)

data = response.json()

print(data)
