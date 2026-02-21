import requests

def get_weather(city: str) -> str:
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)

        if response.status_code != 200:
            return "Sorry, I couldn't fetch the weather."

        data = response.json()
        current = data["current_condition"][0]

        temperature = current["temp_C"]
        description = current["weatherDesc"][0]["value"]

        return f"In {city}, it is currently {description} with a temperature of {temperature}°C."

    except Exception as e:
        return "There was an issue retrieving weather data."