import random
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
from tools import crud, models, schemas
from tools.data import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
PlaneAPI = FastAPI()
def get_db(): # Just getting the db ykyk
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@PlaneAPI.get('/')
def read_root():
    return {"Hey!": "Welcome to PlaneAPI"}

@PlaneAPI.get('/getplane')
def getplane(db: Session = Depends(get_db)):
    all_planes = crud.get_all_planes(db)
    random_plane = random.choice(all_planes)
    return random_plane

@PlaneAPI.get('/getplane/{plane_id}')
def get_a_plane(plane_id,db: Session = Depends(get_db)):
    plane = crud.get_plane_by_id(db, int(plane_id))
    return plane

@PlaneAPI.post("/postplane")
def add_plane(plane:schemas.Plane,db: Session = Depends(get_db)):
    db_plane = crud.get_plane_by_id(db, ids=plane.ids)
    db_plane_name = crud.get_plane_by_name(db, name=plane.name)
    if db_plane:
        raise HTTPException(status_code=400, detail="A plane already exists with the given id.")
    elif db_plane_name:
        raise HTTPException(status_code=400, detail="A plane already exists with the given id.")
    else:
        return crud.create_plane(db=db, plane_info=plane)

#@PlaneAPI.delete("/getplane/{plane_id}")
#def delete_plane(plane_id :int):
#    planedb.pop(plane_id-1)
#    return {"Task": "Deletion successful"}