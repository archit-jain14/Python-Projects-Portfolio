import os
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

console = Console()

def get_weather(city: str):
    if not API_KEY:
        console.print("[bold red]Error:[/] API key missing. Check your .env file.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].capitalize()

        table = Table(title=f"Weather in {city_name}, {country}", style="cyan")
        table.add_column("Metric", style="bold green")
        table.add_column("Value", style="bold white")

        table.add_row("Condition", condition)
        table.add_row("Temperature", f"{temp}°C")
        table.add_row("Feels Like", f"{feels_like}°C")
        table.add_row("Humidity", f"{humidity}%")

        console.print(table)

    except requests.exceptions.HTTPError:
        console.print(f"[bold red]City '{city}' not found or API request failed.[/]")
    except Exception as e:
        console.print(f"[bold red]An error occurred:[/] {e}")

if __name__ == "__main__":
    console.print(Panel.fit("[bold magenta]CLI Weather Tracker[/]"))
    user_city = input("Enter city name: ").strip()
    if user_city:
        get_weather(user_city)