# weather-app
A simple weather API application to check the current weather and forecast across the globe. Made with ❤️ in Python with FastAPI, using [OpenWeather](https://openweathermap.org/api)'s API.


![image](https://user-images.githubusercontent.com/75340355/120859230-4c22a700-c55a-11eb-81c8-57ef271ae508.png)

## Overview
This project was developed using the following technologies and libraries:

Production dependencies
* Python
* Poetry
* FastAPI
* Uvicorn
* python-dotenv
* requests
* xmltodict
* pytz
* cachetools

Dev dependencies
* Flake8
* Autopep8
* Pytest
* httpx
* httpretty
* freezegun


## How to use

### Prerequisites
You will need to have Python 3.9+ and Poetry installed on your computer.

### Getting started
* From your console clone the repository either via url "https://github.com/aldanadc/weather-app.git" or by `running gh repo clone aldanadc/weather-app` from GitHub CLI.
* If you do not have it, install Poetry by running `pip install poetry`.
* Rename the **_.env.sample_** file in the project's root folder to be only .env as these will be your environment variables. The variables you may need are *API_KEY* (mandatory, which you can get for free from OpenWeather's website), *USER_NAME* (optional), *PORT* (optional, in case you want to change FastApi's default which is 8000) and *LOCAL_TIMEZONE* (optional, which will otherwise default to America/Argentina/Buenos_Aires).
* Install all dependencies by running `poetry install --no-root` on the root folder of the cloned project.
* Start the server by running either `poetry run uvicorn weather_api.main:app --port 8080` (make sure you use the correct port in case you change it) or  `poetry run python .\weather_app\weather_api\main.py` from the project's root folder.
* The application is now ready and waiting to be used. The base URL you can access in the browser is http://localhost:{port}/. Make sure you use the correct port if you set one on your **_.env_** file.
* To visit the docs and test the endpoints visit *http:/localhost:{port}/weather-api-service/docs*.


## To do / Improvements
* The caching solution at the moment is very simple and in-memory, in the future a better solution could be to implement something like Redis, for example.
* Deploy the solution to a cloud service.
* Support the option to show data in °C or °F by parameter and not by defaulting to both.


![image](https://user-images.githubusercontent.com/75340355/120859230-4c22a700-c55a-11eb-81c8-57ef271ae508.png)