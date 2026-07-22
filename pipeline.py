from extract import extract_weather, extract_aqi, CITIES
from transform import transform
from load import load

def run_pipeline():
    print("🚀 Starting pipeline...")
    
    for city in CITIES:
        try:
            weather = extract_weather(city)
            aqi = extract_aqi(city)
            record = transform(city, weather, aqi)
            load(record)
        except Exception as e:
            print(f"❌ Failed for {city}: {e}")
    
    print("✅ Pipeline complete!")

if __name__ == "__main__":
    run_pipeline()