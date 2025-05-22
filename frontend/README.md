# Plataforma de Cursos Universitarios

Este proyecto gestiona una base de datos de estudiantes, cursos, profesores, inscripciones y asignaciones usando SQLAlchemy y una interfaz en Streamlit.

## Estructura de carpetas

```bash

plataforma_cursos/
├── bd/                
├── backend/           # Backend (ORM y script de creación)
│   ├── .env.example   # Ejemplo de variables de entorno
│   ├── .env           # Tus credenciales (no commitear)
│   ├── create_and_insert.py  # Script para aplicar schema y data
│   ├── correction_tables.py  # Sincronizar lo modelos del ORM con las tablas
│   ├── crud.py         # Script para definir todo el crud
│   ├── db.py          # Engine y session factory
│   ├── models.py      # Definición de modelos SQLAlchemy
│   └── venv/          # Entorno virtual Python
└── frontend/          
    ├── app.py          # App Streamlit
    └── venv/          # Entorno virtual Python
```



## 0. Iniciar el backend

Primero tuviste que seguir la documentación del backend [BACKEND DOCUMENTATION](https://github.com/CarEsteban/lab3-steamlit/tree/main/backend)

## 1. Ejecutar la aplicación Streamlit

Activa el entorno virtual, instala dependencias y lanza la aplicación:

```bash

cd frontend
source venv/bin/activate   # En Windows: venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```