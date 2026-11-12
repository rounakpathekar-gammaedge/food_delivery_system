from app.database.connection import engine, Base
from app.models.restaurant import Restaurant
from app.models.menu_item import MenuItem
from app.models.user import User

# Create all database tables
Base.metadata.create_all(bind=engine)

print("Database tables created successfully!")