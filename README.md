# India Flight Delay & Air Quality Warehouse

A data engineering pipeline that correlates flight delays at DEL, BOM, and BLR airports with real-time weather and air quality data.

## Data Sources
- Aviationstack API → flight delays
- Open-Meteo API → weather (temperature, wind, visibility, storms)
- OpenAQ API → air quality (PM2.5, PM10, ozone, NO2, SO2)

## Star Schema
- fact_flight_weather
- dim_flight
- dim_airport
- dim_weather
- dim_aqi
- dim_date

## Tech Stack
- Python, Pandas, PostgreSQL, psycopg2, Apache Airflow (coming soon)

## Business Question
Does bad air quality and severe weather correlate with increased flight delays at India's busiest airports?

## Status
🚧 In Progress
