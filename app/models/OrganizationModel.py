from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from configs.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    business_id = Column(Integer, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

    bikes = relationship("Bike", back_populates="owner")
