
import sys, os, datetime

# 1) Asegúrate de que Python puede encontrar el backend
BACKEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
if BACKEND_PATH not in sys.path:
    sys.path.insert(0, BACKEND_PATH)

# 2) Carga variables de entorno desde el .env del backend
from dotenv import load_dotenv # type: ignore
load_dotenv(os.path.join(BACKEND_PATH, ".env"))

# 3) Importa la sesión y tus funciones CRUD / vistas
from db import get_session
from crud import *

import streamlit as st # type: ignore
import pandas as pd # type: ignore

# —––– Interfaz Streamlit –––—  
st.set_page_config(page_title="Vistas Universidad", layout="wide")
st.title("📊 Vistas de la plataforma de cursos")

# Crea una sesión a la base de datos
db = get_session()

# 4) Mostrar vista de inscripciones
with st.expander("Ver tabla de inscripciones"):
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
with st.expander("Ver tabla de asiganciones"):
    st.header("Vista: Cursos y Profesores Asignados")
    teachers = list_course_teachers(db)
    if teachers:
        df_teachers = pd.DataFrame(teachers, columns=[
            "curso_id", "curso_nombre", "profesor_id", "profesor_nombre"
        ])
        st.dataframe(df_teachers, use_container_width=True)
    else:
        st.write("No hay asignaciones para mostrar.")

# 6) Mostrar Estudiantes
with st.expander("👨‍🎓 Ver tabla de estudiantes", expanded=False):
    st.subheader("Listado de estudiantes")
    students = list_estudiantes(db)
    df_students = pd.DataFrame([
        {
            "ID": e.id,
            "Nombre": e.nombre,
            "Email": e.email,
            "Fecha de nacimiento": e.fecha_nacimiento
        }
        for e in students
    ])
    st.dataframe(df_students, use_container_width=True)

# 7) Crear Estudiante
with st.expander("➕ Agregar estudiante", expanded=False):
    st.subheader("Agregar nuevo estudiante")
    with st.form("Crear estudiante"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre")
            fecha_nacimiento = st.date_input("Fecha de nacimiento")
        with col2:
            email = st.text_input("Email")
        submitted = st.form_submit_button("Crear Estudiante")
        if submitted:
            if nombre and email and fecha_nacimiento:
                try:
                    create_estudiante(db, nombre, email, fecha_nacimiento)
                    st.success(f"Estudiante {nombre} creado exitosamente")
                    
                except Exception as e:
                    st.error(f"Error al crear al estudiante: {e}")
            else:
                st.warning("Por favor, llenar todos los campos.")

# 8) Update de un estudiante
with st.expander("✏️ Actualizar estudiante", expanded=False):
    st.subheader("Editar datos de un estudiante")
    students = list_estudiantes(db)
    student_option = {f"{e.id} - {e.nombre}": e for e in students}
    selected = st.selectbox("Selecciona a un estudiante", list(student_option), key="update_select")
    student_selected = student_option[selected]
    with st.form("Actualizar estudiante form"):
        col1, col2 = st.columns(2)
        with col1:
            new_name = st.text_input("Nuevo nombre", value=student_selected.nombre)
        with col2:
            new_email = st.text_input("Nuevo correo", value=student_selected.email)
        fecha_nacimiento = student_selected.fecha_nacimiento
        st.date_input(
            "Fecha de nacimiento (No editable)",
            value=fecha_nacimiento,
            disabled=True
        )
        # Calcular edad
        today = datetime.date.today()
        age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        st.caption(f"Edad: {age} años")
        update_submitted = st.form_submit_button("Actualizar estudiante")
        if update_submitted:
            try:
                update_estudiante(db, student_selected.id, nombre=new_name, email=new_email, fecha_nacimiento=fecha_nacimiento)
                st.success(f"Estudiante {new_name} actualizado exitosamente ")
                
            except Exception as e:
                st.error(f"Error al actualizar: {e}")

# 9) Eliminar estudiante
with st.expander("🗑️ Eliminar estudiante", expanded=False):
    st.subheader("Eliminar un estudiante")
    students = list_estudiantes(db)
    student_option = {f"{e.id} - {e.nombre}": e for e in students}
    selected = st.selectbox("Selecciona a un estudiante a eliminar", list(student_option), key="delete_select")
    student_selected = student_option[selected]
    if st.button("Eliminar estudiante"):
        try:
            delete_estudiante(db, student_selected.id)
            st.success(f"Estudiante {student_selected.nombre} eliminado exitosamente")
            
        except Exception as e:
            st.error(f"Error al eliminar: {e}")