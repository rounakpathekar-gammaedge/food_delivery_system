from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Restaurant(Base):

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    location = Column(String(100), nullable=False)