from pydantic import BaseModel

class Plane(BaseModel):
    ids: int # id
    name: str # plane name
    description: str # just a description tbh
    price: str # plane price
    length: str # plane length
    wingspan: str # wingspan
    mtow: str # maximum takeoff weight
    engine_type: str # does the plane have jet engines or not?
    image: str

