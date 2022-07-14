from typing import List, Union
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from schemas import BikeSchema
from models import BikeModel, OrganizationModel
from services import bike_service
from configs.database import SessionLocal, engine

BikeModel.Base.metadata.create_all(bind=engine)
OrganizationModel.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/bikes/", response_model=BikeSchema.BikeOut)
async def create_bike(bike: BikeSchema.BikeIn, db: Session = Depends(get_db)):
    db_bike = await bike_service.get_bike_by_serial_number(db, serial_number=bike.serial_number)
    if db_bike:
        raise HTTPException(status_code=400, detail="Bike already registered")
    return await bike_service.create_bike(db=db, bike=bike)


@app.put("/bikes/{bike_id}", response_model=BikeSchema.BikeOut)
async def update_bike(bike_id: int, bike: BikeSchema.BikeIn, db: Session = Depends(get_db)):
    db_bike = await bike_service.get_bike(db, bike_id=bike_id)
    if db_bike is None:
        raise HTTPException(status_code=404, detail="Bike not found")
    return await bike_service.update_bike(db_bike=db_bike, db=db, bike=bike)


@app.get("/bikes/", response_model=List[BikeSchema.BikeOut])
async def get_bikes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return await bike_service.get_bikes(db, skip=skip, limit=limit)


@app.get("/bikes/{bike_id}", response_model=BikeSchema.BikeOut)
async def get_bike(bike_id: int, db: Session = Depends(get_db)):
    db_bike = await bike_service.get_bike(db, bike_id=bike_id)
    if db_bike is None:
        raise HTTPException(status_code=404, detail="Bike not found")
    return db_bike


@app.get("/organization/{organization_id}/bikes", response_model=List[BikeSchema.BikeOut])
async def get_bikes_by_organization(
        organization_id: int,
        brand: Union[str, None] = None,
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)):
    return await bike_service.get_bikes_by_organization(
        organization_id=organization_id,
        db=db,
        skip=skip,
        limit=limit,
        brand=brand)


@app.get("/organization/{organization_id}/price")
async def get_organization_bike_avg_price(
        organization_id: int,
        brand: Union[str, None] = None,
        db: Session = Depends(get_db)):
    return await bike_service.get_avg_price_by_organization(
        organization_id=organization_id,
        db=db,
        brand=brand)
