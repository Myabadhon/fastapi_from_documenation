from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0077@localhost:5432/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# # Correct database URL
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:0077@localhost:5432/fastapi"
#
# # Creating the engine
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
#
# # Creating the SessionLocal class
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # Creating the base class for model definitions
# Base = declarative_base()
