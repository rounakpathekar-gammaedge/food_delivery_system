from pydantic import BaseModel, Field
from decimal import Decimal


class MenuItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=300)
    price: Decimal = Field(gt=0)
    available: bool = True


class MenuItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=300)
    price: Decimal | None = Field(default=None, gt=0)
    available: bool | None = None


class MenuItemResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    available: bool
    restaurant_id: int

    model_config = {"from_attributes": True}