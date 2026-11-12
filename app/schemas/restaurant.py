from pydantic import BaseModel, Field


class RestaurantCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    location: str = Field(min_length=2, max_length=100)


class RestaurantResponse(BaseModel):
    id: int
    name: str
    location: str

    model_config = {"from_attributes": True}