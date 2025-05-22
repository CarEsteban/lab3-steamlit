#!/usr/bin/env python3
import os
from sqlalchemy import text, inspect, select, func
from sqlalchemy.orm import Session
from dotenv import load_dotenv

# Importa tu engine y SessionLocal de db.py
from db import engine, SessionLocal
from models import Estudiante, Curso, Profesor, Inscripcion, Asignacion

# Cargar variables de entorno (si aún no lo hace db.py)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

# Rutas a los scripts SQL
BASE_DIR    = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bd"))
SCHEMA_FILE = os.path.join(BASE_DIR, "schema.sql")
DATA_FILE   = os.path.join(BASE_DIR, "data.sql")

def run_sql_file(path: str):
    """Ejecuta todo el SQL contenido en el archivo indicado."""
    with open(path, "r", encoding="utf-8") as f:
        sql = f.read()
    with engine.begin() as conn:
        conn.execute(text(sql))
    print(f"✅ Ejecutado {os.path.basename(path)}")

def tables_exist() -> bool:
    """Comprueba si las tablas principales ya existen en la BD."""
    inspector = inspect(engine)
    existing = inspector.get_table_names()
    required = ["estudiante", "curso", "profesor", "inscripcion", "asignacion"]
    return all(tbl in existing for tbl in required)

def data_loaded() -> bool:
    """Comprueba si al menos una de las tablas principales contiene datos."""
    with SessionLocal() as session:
        for model in (Estudiante, Curso, Profesor, Inscripcion, Asignacion):
            count = session.execute(
                select(func.count()).select_from(model)
            ).scalar_one()
            if count > 0:
                return True
    return False

if __name__ == "__main__":
    # 1) Crear esquema si no existe
    if tables_exist():
        print("⚠️  Tablas ya creadas; se omite schema.sql")
    else:
        print("🚧 Creando tablas...")
        run_sql_file(SCHEMA_FILE)

    # 2) Insertar datos si las tablas están vacías
    if data_loaded():
        print("⚠️  Datos ya ingresados; se omite data.sql")
    else:
        print("🚧 Insertando datos...")
        run_sql_file(DATA_FILE)
