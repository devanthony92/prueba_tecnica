import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

#CARGANDO VARIABLES DE ENTORNO
user_db = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
db_host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
 
#CONFIGURACION DE LA DATABASE
DATABASE_URL = f"mysql+pymysql://{user_db}:{password}@{db_host}:3306/{database}"
engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()