import requests

CITIES = {
    
    "New York":  {"lat": 40.64, "lon": -73.78},  # JFK
    "London":    {"lat": 51.47, "lon": -0.45},   # LHR
    "Dubai":     {"lat": 25.25, "lon": 55.36},   # DXB
    "Singapore": {"lat": 1.35,  "lon": 103.99},  # SIN
    "São Paulo": {"lat": -23.43,"lon": -46.47},  # GRU
    "Sydney":    {"lat": -33.94,"lon": 151.18},  # SYD

}

def extract_weather(city):
    coords = CITIES[city]
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": coords["lat"],
        "longitude": coords["lon"],
        "current": ",".join([
            "temperature_2m",
            "windspeed_10m",
            "winddirection_10m",
            "precipitation",
            "cloudcover",
            "pressure_msl",
            "relativehumidity_2m",
            "weathercode"
        ])
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"✅ Weather extracted for {city}")
        return response.json()["current"]
    else:
        raise Exception(f"❌ Weather failed for {city}: {response.status_code}")

def extract_aqi(city):
    coords = CITIES[city]
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": coords["lat"],
        "longitude": coords["lon"],
        "current": ",".join([
            "pm10",
            "pm2_5",
            "carbon_monoxide",
            "nitrogen_dioxide",
            "ozone",
            "european_aqi"
        ])
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"✅ AQI extracted for {city}")
        return response.json()["current"]
    else:
        raise Exception(f"❌ AQI failed for {city}: {response.status_code}")

if __name__ == "__main__":
    for city in CITIES:
        print(f"\n--- {city} ---")
        weather = extract_weather(city)
        aqi = extract_aqi(city)
        print(f"  Weather: {weather}")
        print(f"  AQI: {aqi}")