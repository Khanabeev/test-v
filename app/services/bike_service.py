from sqlalchemy.orm import Session
from sqlalchemy import func
from models import BikeModel
from schemas import BikeSchema
from typing import Optional


async def get_bike(db: Session, bike_id: int):
    return db.query(BikeModel.Bike).filter(BikeModel.Bike.id == bike_id).first()


async def get_bike_by_serial_number(db: Session, serial_number: str):
    return db.query(BikeModel.Bike).filter(BikeModel.Bike.serial_number == serial_number).first()


async def get_bikes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BikeModel.Bike).offset(skip).limit(limit).all()


async def get_bikes_by_organization(
        organization_id: int,
        db: Session,
        skip: int = 0,
        limit: int = 100,
        brand: Optional[str] = None):
    if not brand:
        return db.query(BikeModel.Bike). \
            filter(BikeModel.Bike.organization == organization_id). \
            offset(skip). \
            limit(limit).all()
    else:
        return db.query(BikeModel.Bike). \
            filter(BikeModel.Bike.organization == organization_id). \
            filter(BikeModel.Bike.brand == brand). \
            offset(skip). \
            limit(limit).all()


async def create_bike(db: Session, bike: BikeSchema.BikeIn):
    db_bike = BikeModel.Bike(
        organization=bike.organization,
        brand=bike.brand,
        model=bike.model,
        price=bike.price,
        serial_number=bike.serial_number,
    )
    db.add(db_bike)
    db.commit()
    db.refresh(db_bike)
    return db_bike


async def update_bike(db_bike: BikeModel, db: Session, bike: BikeSchema.BikeIn):
    db_bike.organization = bike.organization
    db_bike.brand = bike.brand
    db_bike.model = bike.model
    db_bike.price = bike.price
    db_bike.serial_number = bike.serial_number

    db.merge(db_bike)
    db.commit()
    db.refresh(db_bike)
    return db_bike


async def get_avg_price_by_organization(
        organization_id: int,
        db: Session,
        brand: Optional[str] = None):
    if not brand:
        return db.query(func.avg(BikeModel.Bike.price).label('average_price')). \
            filter(BikeModel.Bike.organization == organization_id). \
            all()
    else:
        return db.query(func.avg(BikeModel.Bike.price).label('average_price')). \
            filter(BikeModel.Bike.organization == organization_id). \
            filter(BikeModel.Bike.brand == brand). \
            all()
