import pandas as pd
from datetime import datetime

def transform(city, weather, aqi):
    now = datetime.now()
    
    record = {
        # Date fields
        "timestamp": now,
        "day": now.day,
        "month": now.month,
        "year": now.year,
        "hour": now.hour,
        
        # City
        "city": city,
        
        # Weather
        "temperature": weather["temperature_2m"],
        "windspeed": weather["windspeed_10m"],
        "winddirection": weather["winddirection_10m"],
        "precipitation": weather["precipitation"],
        "cloudcover": weather["cloudcover"],
        "pressure": weather["pressure_msl"],
        "humidity": weather["relativehumidity_2m"],
        "weathercode": weather["weathercode"],
        
        # AQI
        "pm10": aqi["pm10"],
        "pm25": aqi["pm2_5"],
        "carbon_monoxide": aqi["carbon_monoxide"],
        "nitrogen_dioxide": aqi["nitrogen_dioxide"],
        "ozone": aqi["ozone"],
        "european_aqi": aqi["european_aqi"]
    }
    
    return record

if __name__ == "__main__":
    # Test with dummy data
    sample_weather = {
        "temperature_2m": 10.0,
        "windspeed_10m": 6.5,
        "winddirection_10m": 298,
        "precipitation": 0.0,
        "cloudcover": 0,
        "pressure_msl": 1020.0,
        "relativehumidity_2m": 82,
        "weathercode": 0
    }
    sample_aqi = {
        "pm10": 9.6,
        "pm2_5": 9.5,
        "carbon_monoxide": 120.0,
        "nitrogen_dioxide": 25.7,
        "ozone": 17.0,
        "european_aqi": 39
    }
    record = transform("Sydney", sample_weather, sample_aqi)
    print(record)