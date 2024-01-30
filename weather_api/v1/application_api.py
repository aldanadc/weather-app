"""This file contains the controller to manage requests received by the API."""

from fastapi import APIRouter, HTTPException, status
from cachetools import TTLCache
from weather_api.weather_service.weather_service import WeatherService
from weather_api.v1.weather_response_model import WeatherResponse


controller = APIRouter(prefix="/api/v1", tags=["Weather Info ☀️ 🌤️ ☁️ 🌦️ 🌩️"])
weather_cache = TTLCache(maxsize=100, ttl=180)


@controller.get("/weather", response_model=WeatherResponse)
def get_weather_by_city(city: str, country_code: str):
    """Receive city and country and return the weather and forecast for the location.

    Args:
        city (str): name of the city
        country_code (str): country_code as per ISO 3166
 
    Returns:
        dict: formatted current weather and forecast data. If information for that city and country exist in the cache, return that.
        Otherwise, fetch new data, format and return it.
    
    Raises:
        HTTPException: if wrong or no parameters are received
    """

    if not city or not country_code:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"status": status.HTTP_400_BAD_REQUEST, "message": "Please provide data for city and country."})
    if (len(country_code) != 2):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"status": status.HTTP_400_BAD_REQUEST, "message": "country_code should have two characters."})
    if city.isdigit() or country_code.isdigit():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={"status": status.HTTP_400_BAD_REQUEST, "message": "Please provide only strings for city and country."})

    city = city.lower()
    country_code = country_code.lower()
    cached_data = get_data_from_cache(f"{city}, {country_code}")
    if cached_data:
        return cached_data
    else:
        weather_data = WeatherService.get_weather_by_city(city, country_code)
        weather_cache[f"{city}, {country_code}"] = weather_data

        return weather_data


def get_data_from_cache(city: str):
    """Check cache and return data if it exists. Otherwise return None"""
    cached_data = weather_cache.get(city)
    if cached_data:
        return cached_data
    else:
        return None
