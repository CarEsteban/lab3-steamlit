# backend/db.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# 1) Carga las variables de .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# 2) Lee DATABASE_URL o compónla desde partes

# Si prefieres variables separadas:
user = os.getenv("DB_USER")
pwd  = os.getenv("DB_PASS")
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")
name = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql://{user}:{pwd}@{host}:{port}/{name}"

# 3) Crea el engine y la sesión
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session():
    return SessionLocal()
