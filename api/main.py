import random
import sys
import os
import uvicorn
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from fastapi import FastAPI, HTTPException, Depends, Request
from pydantic import BaseModel
from typing import Optional
from tools import crud, models, schemas
from theme import *
from tools.data import SessionLocal, engine
from sqlalchemy.orm import Session
from im import whitelisted


models.Base.metadata.create_all(bind=engine)
PlaneAPI = FastAPI(title="PlaneAPI",description=description,version="1.0.0",contact=contact,openapi_tags=tags_metadata)
def get_db(): # Just getting the db ykyk
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@PlaneAPI.get('/')
def read_root():
    return {"Hey!": "Welcome to PlaneAPI. Use the endpoint `/getplane` to get a random plane!"}

@PlaneAPI.get('/getplane',tags=["Planes"])
def getplane(db: Session = Depends(get_db)):
    all_planes = crud.get_all_planes(db)
    random_plane = random.choice(all_planes)
    return random_plane

@PlaneAPI.get('/getplane/{plane_id}',tags=["Planes"])
def get_a_plane(plane_id,db: Session = Depends(get_db)):
    plane = crud.get_plane_by_id(db, int(plane_id))
    return plane

@PlaneAPI.post("/postplane",tags=["Private Items"])
def add_plane(plane:schemas.Plane,request: Request,db: Session = Depends(get_db)):
    client_host = request.client.host
    if str(client_host) in whitelisted:
        db_plane = crud.get_plane_by_id(db, ids=plane.ids)
        db_plane_name = crud.get_plane_by_name(db, name=plane.name)
        if db_plane:
            raise HTTPException(status_code=400, detail="A plane already exists with the given id.")
        elif db_plane_name:
            raise HTTPException(status_code=400, detail="A plane already exists with the given id.")
        else:
            return crud.create_plane(db=db, plane_info=plane)
    else:
        raise HTTPException(status_code=403, detail="You can't access this...")

@PlaneAPI.delete("/getplane/{plane_id}",tags=["Private Items"])
def delete_plane(plane_id:int,request: Request,db: Session = Depends(get_db)):
    client_host = request.client.host
    if str(client_host) in whitelisted:
        try:
            db_plane = crud.get_plane_by_id(db, ids=int(plane_id))
            res = crud.delete_plane_by_id(db=db, ids=int(plane_id))
        except Exception as e:
                print(e)
                raise HTTPException(status_code=404, detail="Could not find that plane...")
        raise HTTPException(status_code=200, detail="Done!")
    else:
        raise HTTPException(status_code=403, detail="You can't access this...")

if __name__ == "__main__":
    uvicorn.run("main:PlaneAPI", host="127.0.0.1", port=os.getenv("PORT", default=5000), log_level="info")