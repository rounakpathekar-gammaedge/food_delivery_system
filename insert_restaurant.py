from app.database.connection import SessionLocal
from app.models.restaurant import Restaurant

# Create a database session
db = SessionLocal()

try:
    # Create a new restaurant
    new_restaurant = Restaurant(
        name="Burger House",
        location="Indore"
    )

    # Add restaurant to the session
    db.add(new_restaurant)

    # Save changes to PostgreSQL
    db.commit()

    # Refresh the object to get its generated ID
    db.refresh(new_restaurant)

    print("Restaurant added successfully!")
    print("Restaurant ID:", new_restaurant.id)

except Exception as error:
    db.rollback()
    print("Error:", error)

finally:
    db.close()