import requests
import math
import random
from datetime import datetime, timedelta

# API-Schlüssel und URL für OpenWeather
API_KEY = input("Bitte gib deinen OpenWeather API-Schlüssel ein: ")
BASE_URL = "http://api.openweathermap.org/data/2.5/onecall/timemachine"

# Funktion, um historische Wetterdaten von OpenWeather zu erhalten
def get_historical_weather(lat, lon, dt, api_key):
    url = f"{BASE_URL}?lat={lat}&lon={lon}&dt={dt}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    # Überprüfen der Antwort von der API
    if response.status_code == 200:
        data = response.json()
        
        # Prüfen, ob die "current"-Daten vorhanden sind
        if "current" in data:
            temp = data["current"]["temp"]
            return temp
        else:
            print("Fehler: Keine 'current'-Daten in der Antwort gefunden.")
            print("API-Antwort:", data)
            return None
    else:
        print(f"Fehler bei der API-Anfrage: {response.status_code}")
        print("API-Antwort:", response.json())
        return None

# Historische Wetterdaten: Geographische Koordinaten von Zeven
latitude = 53.4411  # Zeven (Breitengrad)
longitude = 9.2349  # Zeven (Längengrad)

# Datum und Zeit für historische Daten (24 Stunden zurück)
current_time = datetime.now()
historical_time = (current_time - timedelta(days=1)).timestamp()

# Hole historische Wetterdaten
historical_temp = get_historical_weather(latitude, longitude, int(historical_time), API_KEY)

if historical_temp is not None:
    # Berechnung der historischen Amplitude (Schwankung der Temperatur)
    historical_avg_temp = historical_temp  # Durchschnittstemperatur aus der API
    historical_amplitude = 2.5  # Diese Amplitude kann in der Realität variieren und wird hier exemplarisch genutzt

    # Schu-Gleichung für Temperaturvorhersage
    def schu_temperature(hour, historical_avg_temp, historical_amplitude):
        # Tageszeitabhängige Amplitude (größere Amplitude am Morgen/Abend)
        time_factor = math.sin(math.pi * (hour / 24))  # Sinuskurve für Tageszeiten
        dynamic_amplitude = historical_amplitude * (1 + time_factor)

        # Berechnung der Temperatur unter Verwendung der historischen Daten und der dynamischen Amplitude
        temp = historical_avg_temp + dynamic_amplitude * math.sin(math.pi * (hour / 12))  # Sinuskurve für Temperaturverlauf
        return temp

    # Zufällige Schwankungen für Windgeschwindigkeit und Feuchtigkeit
    def random_wind_and_humidity():
        wind_speed = random.uniform(0, 15)  # Zufällige Windgeschwindigkeit zwischen 0 und 15 km/h
        humidity = random.uniform(40, 90)   # Zufällige Feuchtigkeit zwischen 40% und 90%
        return wind_speed, humidity

    # Vorhersagezeitraum (24 Stunden)
    forecast_date = datetime(2025, 4, 20)

    # Ausgabe der Vorhersage
    print(f"Schu‑Gleichung‑Vorhersage für Zeven am {forecast_date.strftime('%d.%m.%Y')}")
    print("-" * 70)
    print(f"Zeit                Temp (°C)      Wind (km/h)    Feuchte (%)")

    # Iteration über die Stunden des Vorhersagetages
    for hour in range(24):
        forecast_time = forecast_date + timedelta(hours=hour)
        temp = schu_temperature(hour, historical_avg_temp, historical_amplitude)
        wind_speed, humidity = random_wind_and_humidity()
        print(f"{forecast_time.strftime('%d.%m.%Y %H:%M')}    {temp:.2f}          {wind_speed:.2f}          {humidity:.2f}")
else:
    print("Die historischen Wetterdaten konnten nicht abgerufen werden. Bitte überprüfen Sie die API und den API-Schlüssel.")
