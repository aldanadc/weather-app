"""These file contains test cases for OpenWeatherFormatter."""

from weather_api.weather_service.formatter import OpenWeatherFormatter


def test_get_full_wind_direction():
    result = OpenWeatherFormatter.get_full_wind_direction("NNW")
    assert result == "north-northwest"


def test_convert_to_farenheit():
    result = OpenWeatherFormatter.convert_to_farenheit(25)
    assert result == 77.00
