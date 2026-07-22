import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def get_city_id(cursor, city_name):
    cursor.execute(
        "SELECT city_id FROM dim_city WHERE city_name = %s",
        (city_name,)
    )
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        raise Exception(f"City not found in dim_city: {city_name}")

def load(record):
    conn = get_connection()
    cursor = conn.cursor()

    city_id = get_city_id(cursor, record["city"])

    cursor.execute("""
        INSERT INTO fact_city_conditions (
            city_id, timestamp, day, month, year, hour,
            temperature, windspeed, winddirection, precipitation,
            cloudcover, pressure, humidity, weathercode,
            pm10, pm25, carbon_monoxide, nitrogen_dioxide,
            ozone, european_aqi
        ) VALUES (
            %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s
        )
    """, (
        city_id,
        record["timestamp"], record["day"], record["month"],
        record["year"], record["hour"],
        record["temperature"], record["windspeed"],
        record["winddirection"], record["precipitation"],
        record["cloudcover"], record["pressure"],
        record["humidity"], record["weathercode"],
        record["pm10"], record["pm25"],
        record["carbon_monoxide"], record["nitrogen_dioxide"],
        record["ozone"], record["european_aqi"]
    ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Loaded record for {record['city']}")