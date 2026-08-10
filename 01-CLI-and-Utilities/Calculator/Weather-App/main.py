import requests


def get_weather(city_name):
    # Public OpenWeather API wrapper endpoint (or standard wttr.in JSON format)
    url = f"https://wttr.in/{city_name}?format=j1"

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(
                f"❌ Unable to find weather details for '{city_name}'. Please check the city name."
            )
            return

        data = response.json()
        current_condition = data["current_condition"][0]

        temp_c = current_condition["temp_C"]
        feels_like = current_condition["FeelsLikeC"]
        humidity = current_condition["humidity"]
        weather_desc = current_condition["weatherDesc"][0]["value"]
        wind_speed = current_condition["windspeedKmph"]

        print("\n" + "=" * 45)
        print(f"🌤️  WEATHER REPORT: {city_name.upper()}")
        print("=" * 45)
        print(f"🌡️  Temperature   : {temp_c}°C (Feels like {feels_like}°C)")
        print(f"☁️  Condition     : {weather_desc}")
        print(f"💧 Humidity      : {humidity}%")
        print(f"💨 Wind Speed     : {wind_speed} km/h")
        print("=" * 45)

    except requests.exceptions.RequestException:
        print("❌ Network Error: Unable to fetch weather data.")
    except (KeyError, IndexError):
        print("❌ Error: Invalid response format received from weather service.")


def main():
    print("=" * 45)
    print("🌍 Welcome to CLI Weather Tracker! 🌍")
    print("=" * 45)

    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("\n👋 Stay safe and have a great day!")
            break

        if city:
            print(f"⏳ Fetching live weather for '{city}'...")
            get_weather(city)
        else:
            print("⚠️ City name cannot be empty.")


if __name__ == "__main__":
    main()