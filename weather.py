import requests


def get_weather(city):
    api_key = "f0f6c5a0f3d6e47ba8621ccad5a5367f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    final_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(final_url).json()
    return weather_data



