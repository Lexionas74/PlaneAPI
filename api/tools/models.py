from sqlalchemy import Boolean, Column, Integer, String
from .data import Base
class Plane(Base):
    __tablename__ = "planes"

    ids = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True) # plane name
    description = Column(String, index=True)
    price = Column(String, index=True) # plane price
    length = Column(String, index=True) # plane length
    wingspan = Column(String, index=True) # wingspan
    mtow = Column(String, index=True) # maximum takeoff weight
    engine = Column(String, index=True) #what type of engine is it? turboprop? jet?
    image = Column(String, index=True) # image
