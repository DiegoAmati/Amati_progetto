from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Path to the database file
db_path = 'sqlite:///users.db'

# Create an engine and connect to the database
engine = create_engine(db_path)
metadata = MetaData()

# Reflect the tables
metadata.reflect(bind=engine)

# Drop all tables
metadata.drop_all(bind=engine)

print("All tables have been deleted successfully.")