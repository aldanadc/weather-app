"""These file contains test cases for OpenWeatherConsumer & WeatherService."""

import json
import re
import httpretty
from fastapi.testclient import TestClient
from freezegun import freeze_time
from weather_api.main import app
from .mocks import (mocked_get_coordinates_value,
                    mocked_get_weather_value,
                    mocked_get_forecast_value,
                    mocked_get_weather_by_city_value,
                    mocked_invalid_city_response_value,
                    mocked_invalid_lon_response_value,
                    mocked_invalid_lat_response_value)


client = TestClient(app)


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_invalid_longitud():
    httpretty.register_uri(httpretty.GET, re.compile(r"http://api.openweathermap.org/geo/1.0/direct"),
                           body=json.dumps(mocked_get_coordinates_value), status=200)
    httpretty.register_uri(httpretty.GET, re.compile(r"https://api.openweathermap.org/data/2.5/weather"),
                           body=json.dumps(mocked_invalid_lon_response_value), status=400)

    response = client.get("/api/v1/weather?city=dublin&country_code=ie")
    assert response.status_code == 400
    assert response.json() == {"detail": {
        "status": 400, "message": "An error ocurred, please try again."}}


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_invalid_latitutde():
    httpretty.register_uri(httpretty.GET, re.compile(r"http://api.openweathermap.org/geo/1.0/direct"),
                           body=json.dumps(mocked_get_coordinates_value), status=200)
    httpretty.register_uri(httpretty.GET, re.compile(r"https://api.openweathermap.org/data/2.5/weather"),
                           body=mocked_get_weather_value, status=200)
    httpretty.register_uri(httpretty.GET, re.compile(r"https://api.openweathermap.org/data/2.5/forecast"),
                           body=json.dumps(mocked_invalid_lat_response_value), status=400)

    response = client.get("/api/v1/weather?city=dublin&country_code=ie")
    assert response.status_code == 400
    assert response.json() == {"detail": {
        "status": 400, "message": "An error ocurred, please try again."}}


@freeze_time("2024-01-29 18:31:52", tz_offset=+3)
@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_successfully():
    httpretty.register_uri(httpretty.GET, re.compile(r"http://api.openweathermap.org/geo/1.0/direct"),
                           body=json.dumps(mocked_get_coordinates_value), status=200)
    httpretty.register_uri(httpretty.GET, re.compile(r"https://api.openweathermap.org/data/2.5/weather"),
                           body=mocked_get_weather_value, status=200)
    httpretty.register_uri(httpretty.GET, re.compile(r"https://api.openweathermap.org/data/2.5/forecast"),
                           body=json.dumps(mocked_get_forecast_value), status=200)

    response = client.get("/api/v1/weather?city=dublin&country_code=ie")
    assert response.status_code == 200
    assert response.json() == mocked_get_weather_by_city_value


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_invalid_city():
    httpretty.register_uri(httpretty.GET, re.compile(r"http://api.openweathermap.org/geo/1.0/direct"),
                           body=json.dumps(mocked_invalid_city_response_value), status=404)

    response = client.get(
        "/api/v1/weather?city=dublinnnnnnnnnnn&country_code=ie")
    assert response.status_code == 404
    assert response.json() == {"detail": {
        "status": 404, "message": "An error ocurred, please try again."}}


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_city_is_numeric():
    response = client.get("/api/v1/weather?city=46464&country_code=ie")
    assert response.status_code == 400
    assert response.json() == {"detail": {
        "status": 400, "message": "Please provide only strings for city and country."}}


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_no_params():
    response = client.get("/api/v1/weather?city=dublin&country_code=")
    assert response.status_code == 400
    assert response.json() == {"detail": {
        "status": 400, "message": "Please provide data for city and country."}}


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_invalid_country():
    response = client.get("/api/v1/weather?city=dublin&country_code=iee")
    assert response.status_code == 400
    assert response.json() == {"detail": {
        "status": 400, "message": "country_code should have two characters."}}


@httpretty.activate(verbose=True, allow_net_connect=False)
def test_get_weather_city_not_found():
    httpretty.register_uri(httpretty.GET, re.compile(r"http://api.openweathermap.org/geo/1.0/direct"),
                           body=json.dumps([]), status=200)

    response = client.get(
        "/api/v1/weather?city=dublinnnnnnnnnnnn&country_code=ie")
    assert response.status_code == 404
    assert response.json() == {"detail": {
        "status": 404, "message": "We couldn't find any location with the data provided."}}
