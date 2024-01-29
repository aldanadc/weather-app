import os
from datetime import datetime
from dotenv import load_dotenv
import pytz

load_dotenv()

LOCAL_TIMEZONE = pytz.timezone(
    os.getenv("LOCAL_TIMEZONE", "America/Argentina/Buenos_Aires"))
UTC_TIMEZONE = pytz.timezone("UTC")
CARDINAL_POINTS = {
    "E": "east",
    "W": "west",
    "S": "south",
    "N": "north"
}


class OpenWeatherFormatter():

    """Class which contains helper methods to format and convert data.

    Methods:
        format_current_weather(cls, city, api_response):
            Given the city and api_response, format the current weather data in a dict as necessary for the response

        format_forecast(cls, city, forecast_data):
            Given the city and forecast_data, format the forecasted weather data in a dict as necessary for the response

        get_full_wind_direction(cls, direction):
            Given a string of letters representing the wind directions, format the same in full text

        convert_to_farenheit(cls, celsius):
            Given a number representing temperature in celsius, convert it to fahrenheit
    """

    @classmethod
    def format_current_weather(cls, city: str, api_response: dict):
        current_weather = api_response["current"]
        local_time = datetime.now(LOCAL_TIMEZONE)
        utc_sunrise = datetime.strptime(
            current_weather['city']['sun']['@rise'], '%Y-%m-%dT%H:%M:%S')
        utc_sunset = datetime.strptime(
            current_weather['city']['sun']['@set'], '%Y-%m-%dT%H:%M:%S')
        local_sunrise = UTC_TIMEZONE.localize(
            utc_sunrise).astimezone(LOCAL_TIMEZONE)
        local_sunset = UTC_TIMEZONE.localize(
            utc_sunset).astimezone(LOCAL_TIMEZONE)
        result = {
            "location_name": f"{city.title()}, {current_weather['city']['country']}",
            "temperature_c": f"{current_weather['temperature']['@value']} °C",
            "temperature_f": f"{cls.convert_to_farenheit(float(current_weather['temperature']['@value']))} °F",
            "wind": f"{current_weather['wind']['speed']['@name']}, {current_weather['wind']['speed']['@value']}"
            f"{current_weather['wind']['speed']['@unit']}, {cls.get_full_wind_direction(current_weather['wind']['direction']['@code'])}",
            "cloudiness": f"{current_weather['clouds']['@name'].capitalize()}",
            "pressure": f"{current_weather['pressure']['@value']} {current_weather['pressure']['@unit'].lower()}",
            "humidity": f"{current_weather['humidity']['@value']}{current_weather['humidity']['@unit']}",
            "sunrise": f"{local_sunrise.strftime('%H:%M')}",
            "sunset": f"{local_sunset.strftime('%H:%M')}",
            "geocoordinates": f"[{current_weather['city']['coord']['@lat']}, {current_weather['city']['coord']['@lon']}]",
            "requested_time": local_time.strftime("%Y-%m-%d, %H:%M:%S")
        }
        return result

    @classmethod
    def format_forecast(cls, forecast_data: list[dict]):
        response = {}
        for forecast in forecast_data:
            utc_time = datetime.strptime(
                forecast["dt_txt"], '%Y-%m-%d %H:%M:%S')
            local_time = UTC_TIMEZONE.localize(
                utc_time).astimezone(LOCAL_TIMEZONE)
            local_time = local_time.strftime("%Y-%m-%d %Hhs")
            response[local_time] = {
                "weather": f"{forecast['weather'][0]['description'].capitalize()}",
                "temperature_c": f"{forecast['main']['temp']} °C",
                "temperature_f": f"{cls.convert_to_farenheit(float(forecast['main']['temp']))} °F",
                "max_temperature_c": f"{forecast['main']['temp_max']} °C",
                "max_temperature_f": f"{cls.convert_to_farenheit(float(forecast['main']['temp_max']))} °F",
                "min_temperature_c": f"{forecast['main']['temp_min']} °C",
                "min_temperature_f": f"{cls.convert_to_farenheit(float(forecast['main']['temp_min']))} °F",
                "feels_like_c": f"{forecast['main']['feels_like']} °C",
                "feels_like_f": f"{cls.convert_to_farenheit(float(forecast['main']['feels_like']))} °F",
                "humidity": f"{forecast['main']['humidity']}%",
                "clouds": f"{forecast['clouds']['all']}%",
                "precipitation_probability": f"{round(forecast['pop'] * 100)}%",
                "pressure": f"{forecast['main']['pressure']} hpa",
                "wind_speed": f"{forecast['wind']['speed']} m/s",
                "visibility": f"{forecast['visibility']} m",
            }
        return response

    @staticmethod
    def get_full_wind_direction(direction: str):
        if len(direction) == 1:
            return CARDINAL_POINTS[direction]
        elif len(direction) == 2:
            return CARDINAL_POINTS[direction[0]]+CARDINAL_POINTS[direction[1]]
        elif len(direction) == 3:
            return f"{CARDINAL_POINTS[direction[0]]}-{CARDINAL_POINTS[direction[1]]}{CARDINAL_POINTS[direction[2]]}"

    @staticmethod
    def convert_to_farenheit(celsius: float):
        fahrenheit = celsius * 9/5 + 32
        return round(fahrenheit, 2)
