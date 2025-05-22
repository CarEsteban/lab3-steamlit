import sys, os
# 1) Inserta el path al backend
BACKEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

# 2) Carga variables de entorno (dotenv)
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "backend", ".env"))

# A partir de aquí ya puedes importar db, crud, models, etc.
from db import get_session
from crud import list_estudiantes, create_estudiante
import streamlit as st
from datetime import date


# —––– INTERFAZ –––—  
st.title("👩‍🎓 Plataforma de Cursos – Test Conexión Backend")

# Botón para crear un estudiante de prueba
if st.button("Crear estudiante de prueba"):
    db = get_session()
    nuevo = create_estudiante(db, "Frontend Test", "frontend@test.edu", date(2000,1,1))
    st.success(f"🎉 Creado: {nuevo}")

# Listado de estudiantes
st.header("Lista de estudiantes actuales")
db = get_session()
estudiantes = list_estudiantes(db, limit=10)
# Muestra como DataFrame o como lista
st.write(estudiantes)  # gracias al __repr__ verás cada objeto con sus campos
# O, si prefieres tabla:
# import pandas as pd
# df = pd.DataFrame([{"id": e.id, "nombre": e.nombre, "email": e.email} for e in estudiantes])
# st.dataframe(df)