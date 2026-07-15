
-- Dimension: Date
CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    full_timestamp TIMESTAMP,
    day INT,
    month INT,
    year INT,
    hour INT,
    season VARCHAR(20)  -- Summer/Monsoon/Winter/Spring
);

-- Dimension: Airport
CREATE TABLE dim_airport (
    airport_id SERIAL PRIMARY KEY,
    airport_name VARCHAR(100),
    iata_code VARCHAR(10) UNIQUE,
    city VARCHAR(50),
    state VARCHAR(50)
);

-- Dimension: Flight
CREATE TABLE dim_flight (
    flight_id SERIAL PRIMARY KEY,
    flight_number VARCHAR(20),
    airline VARCHAR(100),
    origin_iata VARCHAR(10),
    destination_iata VARCHAR(10),
    scheduled_departure TIMESTAMP,
    scheduled_arrival TIMESTAMP
);

-- Dimension: Weather
CREATE TABLE dim_weather (
    weather_id SERIAL PRIMARY KEY,
    temperature NUMERIC,
    feels_like NUMERIC,
    humidity INT,
    pressure NUMERIC,
    visibility NUMERIC,
    wind_speed NUMERIC,
    wind_direction INT,
    gust_speed NUMERIC,
    cloud_coverage INT,
    condition VARCHAR(50),
    rain_last_hour NUMERIC
);

-- Dimension: AQI
CREATE TABLE dim_aqi (
    aqi_id SERIAL PRIMARY KEY,
    aqi_value INT,
    aqi_category VARCHAR(30),
    pm25 NUMERIC,
    pm10 NUMERIC,
    ozone NUMERIC,
    no2 NUMERIC,
    so2 NUMERIC,
    co NUMERIC,
    dominant_pollutant VARCHAR(20)
);

-- Fact Table
CREATE TABLE fact_flight_weather (
    sighting_id SERIAL PRIMARY KEY,
    date_id INT REFERENCES dim_date(date_id),
    flight_id INT REFERENCES dim_flight(flight_id),
    airport_id INT REFERENCES dim_airport(airport_id),
    weather_id INT REFERENCES dim_weather(weather_id),
    aqi_id INT REFERENCES dim_aqi(aqi_id),
    delay_mins INT,
    flight_count INT,
    is_delayed BOOLEAN,
    is_cancelled BOOLEAN,
    delay_reason VARCHAR(50)
);

-- Seed airport data
INSERT INTO dim_airport (airport_name, iata_code, city, state) VALUES
('Indira Gandhi International Airport', 'DEL', 'Delhi', 'Delhi'),
('Chhatrapati Shivaji Maharaj International Airport', 'BOM', 'Mumbai', 'Maharashtra'),
('Kempegowda International Airport', 'BLR', 'Bengaluru', 'Karnataka');