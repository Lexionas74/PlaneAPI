from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

PlaneAPI = FastAPI()

@PlaneAPI.get('/')
def read_root():
    return {"Hey!": "Welcome to PlaneAPI"}