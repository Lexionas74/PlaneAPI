from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

PlaneAPI = FastAPI()

planedb = []

class Plane(BaseModel):
    id: int
    name: str
    price: str
    length: str
    winspan: str
    is_jet_engine: Optional[bool] = None

@PlaneAPI.get('/')
def read_root():
    return {"Hey!": "Welcome to PlaneAPI"}

@PlaneAPI.get('/getplane')
def getplane():
    return planedb

@PlaneAPI.get('/getplane/{plane_id}')
def get_a_plane(plane_id: int):
    plane = plane_id - 1
    return planedb[plane]

@PlaneAPI.post("/getplane")
def add_plane(plane: Plane):
    planedb.append(plane.dict())
    return planedb[-1]  

@PlaneAPI.delete("/getplane/{plane_id}")
def delete_plane(plane_id :int):
    planedb.pop(plane_id-1)
    return {"Task": "Deletion successful"}