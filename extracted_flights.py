import pandas as pd

def extract_flights(filepath):
    print("Extracting flight data...")
    df = pd.read_csv(filepath)
    print(f" Extracted {len(df)} rows")
    print(df.head())
    return df

if __name__ == "__main__":
    df = extract_flights("india_flight_weather.csv")