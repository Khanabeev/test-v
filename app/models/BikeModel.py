from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from configs.database import Base


class Bike(Base):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True, index=True)
    organization = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=True)
    price = Column(Numeric, nullable=False)
    serial_number = Column(String, unique=True, nullable=False)

    owner = relationship("Organization", back_populates="bikes")
