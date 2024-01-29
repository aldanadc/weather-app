from pydantic import BaseModel


class WeatherResponse(BaseModel):
    """Class that represents the response of the get weather endpoint"""
    location_name: str
    temperature_c: str
    temperature_f: str
    wind: str
    cloudiness: str
    pressure: str
    humidity: str
    sunrise: str
    sunset: str
    geocoordinates: str
    requested_time: str
    forecast: dict
