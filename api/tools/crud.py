from sqlalchemy.orm import Session
from sqlalchemy import delete
from . import models, schemas


def get_all_planes(db: Session):
    return db.query(models.Plane).all()

def get_plane_by_id(db: Session, ids: int):
    return db.query(models.Plane).filter(models.Plane.ids == ids).first()

def get_plane_by_name(db: Session, name: str):
    return db.query(models.Plane).filter(models.Plane.name == name).first()

def create_plane(db: Session, plane_info: schemas.Plane):
    db_user = models.Plane(ids=plane_info.ids, name=plane_info.name, description=plane_info.description, price=plane_info.price, length=plane_info.length, wingspan=plane_info.wingspan, mtow=plane_info.mtow, engine_type=plane_info.engine_type, image=plane_info.image)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_plane_by_id(db:Session,ids: int):
    db.query(models.Plane).filter(models.Plane.ids == ids).delete()
    db.commit()
    return True
