import requests
import time
from datetime import datetime, timedelta
#© Dominic Schu, 2025 – Alle Rechte vorbehalten.
# === HIER DEIN API-KEY ===
API_KEY = "API_KEY"  # <-- Ersetze diesen String durch deinen tatsächlichen API-Key

# OpenWeather API URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Liste der Städte
cities = ["Berlin", "München", "Hamburg", "Köln"]

# Funktion: Wetterdaten für eine Stadt abrufen
def get_weather_data(city):
    try:
        url = f"{BASE_URL}?q={city},de&appid={API_KEY}&units=metric&lang=de"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            weather_description = data['weather'][0]['description']
            return temperature, humidity, pressure, weather_description
        else:
            print(f"Fehler bei der Wetterabfrage für {city}: {data.get('message', 'Unbekannter Fehler')}")
            return None
    except Exception as e:
        print(f"Fehler beim Abrufen der Wetterdaten für {city}: {e}")
        return None

# Funktion: Ausgabe und Logging
def log_and_alert(city, temperature, humidity, pressure, weather_description):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    alert_threshold = 30  # °C

    log_message = f"{current_time} - {city}: Temp={temperature}°C, Humidity={humidity}%, Pressure={pressure} hPa, Wetter={weather_description}"

    if temperature > alert_threshold:
        print(f"\033[91m{log_message}\033[0m")  # Rot bei Alarm
        with open("log.txt", "a") as log_file:
            log_file.write(f"ALERT! {log_message}\n")
    else:
        print(log_message)
        with open("log.txt", "a") as log_file:
            log_file.write(f"{log_message}\n")

# Funktion: Überprüfung des Wetters der letzten 5 Tage
def check_weather():
    for city in cities:
        print(f"🔍 Überprüfe Wetterdaten für {city}...")
        for day in range(1, 6):  # Tage 1 bis 5
            past_date = (datetime.now() - timedelta(days=day)).strftime('%Y-%m-%d')
            print(f"→ {past_date}")
            weather_data = get_weather_data(city)
            if weather_data:
                temperature, humidity, pressure, weather_description = weather_data
                log_and_alert(city, temperature, humidity, pressure, weather_description)
            time.sleep(1)

# Hauptfunktion: Endlosschleife
def main():
    while True:
        check_weather()
        print("⏳ Warte 60 Sekunden bis zur nächsten Überprüfung...\n")
        time.sleep(60)

# Start
if __name__ == "__main__":
    main()
