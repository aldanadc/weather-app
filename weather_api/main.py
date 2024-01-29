#!/usr/bin/env python

"""
Launcher file of the application.

This API service is based on FastAPI, for more info please refer to: https://fastapi.tiangolo.com/.
You will need to have your environments variables set up before running this file.

Author: Aldana D. Casal
"""
import os
import uvicorn
from fastapi import FastAPI, Request
from dotenv import load_dotenv
from weather_api.v1.application_api import controller
from fastapi.responses import JSONResponse


app = FastAPI(
    title="Weather API service documentation page",
    docs_url="/weather-api-service/docs",
    redoc_url="/weather-api-service/redoc",
    openapi_url="/weather/api/v1/openapi.json",
)


load_dotenv()
app.include_router(controller)


@app.get("/")
def home_route():
    user = os.getenv("USER_NAME", "guest user")
    return {"message": f"Welcome to this API's home page, {user}."}


@app.exception_handler(Exception)
def catch_all_exceptions(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"status_code": 500,
                 "message": "Something went wrong, please try again."},
    )


if __name__ == "__main__":
    uvicorn.run("main:app", port=int(os.getenv("PORT", 8080)))
