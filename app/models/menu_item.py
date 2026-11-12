from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric

from app.database.connection import Base


class MenuItem(Base):

    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    description = Column(String(300))

    price = Column(Numeric(10, 2), nullable=False)

    available = Column(Boolean, default=True)

    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id"),
        nullable=False
    )