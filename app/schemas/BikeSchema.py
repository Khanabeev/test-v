from pydantic import BaseModel
from enum import Enum


class Brand(str, Enum):
    canyon = "Canyon",
    trek = "Trek",
    cannondale = "Cannondale",
    specialized = "Specialized",
    giant = "Giant",
    orbea = "Orbea",
    scott = "Scott",
    santa_cruz = "Santa Cruz"
    cervelo = "Cervelo"


class BikeBase(BaseModel):
    id: int
    organization: int
    brand: Brand
    model: str
    price: float
    serial_number: str

    class Config:
        orm_mode = True


class BikeIn(BaseModel):
    organization: int
    brand: Brand
    model: str
    price: float
    serial_number: str

    class Config:
        orm_mode = True


class BikeOut(BaseModel):
    id: str
    organization: int
    brand: Brand
    model: str
    price: float
    serial_number: str

    class Config:
        orm_mode = True


class BikeAvgPrice(BaseModel):
    organization: int
    avg_price: float

    class Config:
        orm_mode = True
