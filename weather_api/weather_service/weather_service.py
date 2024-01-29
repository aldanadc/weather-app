import os
import requests
from dotenv import load_dotenv
import xmltodict
from fastapi import HTTPException
from weather_api.weather_service.formatter import OpenWeatherFormatter

load_dotenv()
API_KEY = os.getenv("API_KEY")


class OpenWeatherConsumer:
    """Class to interact with external Open Weather Map API

    Attributes:
        geocoding_base_url (string): Base url to get geocoordinates for a city
        current_weather_base_url (string):  Base url to get current weather for city given its set of coordinates
        forecast_base_url (string):  Base url to get forecast information for a city given its set of coordinates

    Methods:
        get_coordinates(self, city, country_code):
            Call make_request with the endpoint for getting geocoordinates from Open Weather Maps API and return the response

        get_weather(self, lat, lon):
            Call make_request with the endpoint for getting current weather from Open Weather Maps API and return the response

        get_forecast(self, lat, lon):
            Call make_request with the endpoint for getting forecasted weather from Open Weather Maps API and return the response

    """
    geocoding_base_url = "http://api.openweathermap.org/geo/1.0/direct"
    current_weather_base_url = "https://api.openweathermap.org/data/2.5/weather"
    forecast_base_url = "https://api.openweathermap.org/data/2.5/forecast"

    @classmethod
    def _make_request(cls, url: str):
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code,
                                detail={"status": response.status_code,
                                        "message": "An error ocurred, please try again."})
        return response

    @classmethod
    def get_coordinates(cls, city: str, country_code: str):
        geocoding_endpoint = f"{cls.geocoding_base_url}?q={city},{country_code}&limit=1&appid={API_KEY}"
        return cls._make_request(geocoding_endpoint).json()

    @classmethod
    def get_weather(cls, lat: float, lon: float):
        weather_endpoint = f"{cls.current_weather_base_url}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&mode=xml"
        weather_response = cls._make_request(weather_endpoint)
        return xmltodict.parse(weather_response.content)

    @classmethod
    def get_forecast(cls, lat: float, lon: float):
        forecast_endpoint = f"{cls.forecast_base_url}?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        return cls._make_request(forecast_endpoint).json()


class WeatherService():
    """Class which interacts with OpenWeatherConsumer and Formatter to provide formatted weather data

    Methods:
        get_weather_by_city(self, city, country_code):
            Given the city and country_code, call the necessary functions and return formatted weather information

    Raises:
        HTTPException: if no city is found with the provided parameters

    Returns: dict with the format of the class WeatherResponse
    """

    @staticmethod
    def get_weather_by_city(city: str, country_code: str):
        coordinates_response = OpenWeatherConsumer.get_coordinates(
            city, country_code)
        try:
            lat = coordinates_response[0]["lat"]
            lon = coordinates_response[0]["lon"]
        except Exception:
            raise HTTPException(status_code=404,
                                detail={"status": 404, "message": "We couldn't find any location with the data provided."})

        weather_response = OpenWeatherConsumer.get_weather(lat, lon)
        formatted_response = OpenWeatherFormatter.format_current_weather(
            city, weather_response)
        forecast_response = OpenWeatherConsumer.get_forecast(lat, lon)
        formatted_response["forecast"] = OpenWeatherFormatter.format_forecast(
            forecast_response["list"])
        return formatted_response
