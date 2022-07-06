from pydantic import BaseModel

class Plane(BaseModel):
    ids: int # id
    name: str # plane name
    description: str # just a description tbh
    price: str # plane price
    length: str # plane length
    wingspan: str # wingspan
    mtow: str # maximum takeoff weight
    engine: str # engine type
    image: str # plane image


