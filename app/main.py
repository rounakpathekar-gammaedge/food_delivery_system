from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantCreate, RestaurantResponse
from app.models.menu_item import MenuItem
from app.models.user import User

from app.schemas.user import UserCreate, UserResponse

from app.core.security import hash_password

from sqlalchemy.exc import IntegrityError

from app.schemas.menu_item import (
    MenuItemCreate,
    MenuItemUpdate,
    MenuItemResponse
)

app = FastAPI(
    title="Food Delivery Management System",
    description="Backend API for food delivery",
    version="1.0.0"
)


@app.get("/")
async def home():
    return {
        "message": "Welcome to Food Delivery Management System",
        "status": "Running"
    }


@app.post("/restaurants", response_model=RestaurantResponse)
def create_restaurant(
    restaurant: RestaurantCreate,
    db: Session = Depends(get_db)
):
    new_restaurant = Restaurant(
        name=restaurant.name,
        location=restaurant.location
    )

    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return new_restaurant


@app.get("/restaurants", response_model=list[RestaurantResponse])
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()

@app.post(
    "/restaurants/{restaurant_id}/menu-items",
    response_model=MenuItemResponse
)
def create_menu_item(
    restaurant_id: int,
    item: MenuItemCreate,
    db: Session = Depends(get_db)
):
    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    if restaurant is None:
        raise HTTPException(
            status_code=404,
            detail="Restaurant not found"
        )

    new_item = MenuItem(
        name=item.name,
        description=item.description,
        price=item.price,
        available=item.available,
        restaurant_id=restaurant_id
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    return new_item

@app.post("/register", response_model=UserResponse, status_code=201)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    new_user = User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    return new_user