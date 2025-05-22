
import sys, os

# 1) Asegúrate de que Python puede encontrar el backend
BACKEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

# 2) Carga variables de entorno desde el .env del backend
from dotenv import load_dotenv
load_dotenv(os.path.join(BACKEND_PATH, ".env"))

# 3) Importa la sesión y tus funciones CRUD / vistas
from db import get_session
from crud import list_course_enrollments, list_course_teachers

import streamlit as st
import pandas as pd

# —––– Interfaz Streamlit –––—  
st.set_page_config(page_title="Vistas Universidad", layout="wide")
st.title("📊 Vistas de la plataforma de cursos")

# Crea una sesión a la base de datos
db = get_session()

# 4) Mostrar vista de inscripciones
st.header("Vista: Cursos e Inscripciones")
enrolls = list_course_enrollments(db)
if enrolls:
    df_enrolls = pd.DataFrame(enrolls, columns=[
        "estudiante_id", "estudiante_nombre", "curso_id", "curso_nombre", "estado"
    ])
    st.dataframe(df_enrolls, use_container_width=True)
else:
    st.write("No hay inscripciones para mostrar.")

# 5) Mostrar vista de asignaciones (cursos y profesores)
st.header("Vista: Cursos y Profesores Asignados")
teachers = list_course_teachers(db)
if teachers:
    df_teachers = pd.DataFrame(teachers, columns=[
        "curso_id", "curso_nombre", "profesor_id", "profesor_nombre"
    ])
    st.dataframe(df_teachers, use_container_width=True)
else:
    st.write("No hay asignaciones para mostrar.")
