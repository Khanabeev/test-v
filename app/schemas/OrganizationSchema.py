from typing import List
from pydantic import BaseModel
from schemas.BikeSchema import BikeOut


class Organization(BaseModel):
    id: int
    name: str
    business_id: str
    email: str

    bikes: List[BikeOut] = []

    class Config:
        orm_mode = True
