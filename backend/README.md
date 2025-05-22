# Plataforma de Cursos Universitarios

Este proyecto gestiona una base de datos de estudiantes, cursos, profesores, inscripciones y asignaciones usando SQLAlchemy y una interfaz en Streamlit.

## Estructura de carpetas

```bash

plataforma_cursos/
├── bd/                # SQL scripts: schema.sql, data.sql
├── backend/           # Backend (ORM y script de creación)
│   ├── .env.example   # Ejemplo de variables de entorno
│   ├── .env           # Tus credenciales (no commitear)
│   ├── create_tables.py  # Script para aplicar schema y data
│   ├── db.py          # Engine y session factory
│   ├── models.py      # Definición de modelos SQLAlchemy
│   └── venv/          # Entorno virtual Python
└── frontend/          # App Streamlit
    ├── app.py
    └── venv/          # Entorno virtual Python
```


## Requisitos previos

- Python 3.8+  
- PostgreSQL instalado y en ejecución  

## 1. Crear la base de datos en PostgreSQL

Abre tu consola `psql` como superusuario o usuario con permisos:

```sql
CREATE DATABASE lab3_cursos_universitarios OWNER <tu_usuario>;
```

## 2. Backend: configurar entorno y credenciales

Dentro de backend/

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Luego copia el ejemplo y crea tu propio .env:

```bash
cp .env.example .env
```

Edita .env con tus credenciales:

```bash
DB_USER=tu_user
DB_PASS=tu_password
DB_HOST=localhost
DB_PORT=tu_puerto
DB_NAME=lab3_cursos_universitarios 
```

## 3. Creación de las tablas

Ejecuta el siguiente script:

```bash
python create_and_insert_bd.py
```

Si todo esta bien conetado debería mostrarte en pantalla que todo fue ingresado con éxito!


## 4. Prueba

Si todo te funciona correctamente ejecuta el script test.py

```bash
python test.py
```

Si te da un resultado parecido a este:

```bash
[<Estudiante(id=1, nombre='Ana Gómez', email='ana.gomez@uni.edu')>, <Estudiante(id=2, nombre='Bruno Martínez', email='bruno.martinez@uni.edu')>, <Estudiante(id=3, nombre='Carla Ruiz', email='carla.ruiz@uni.edu')>, <Estudiante(id=4, nombre='Diego Fernández', email='diego.fernandez@uni.edu')>, <Estudiante(id=5, nombre='Elena Castillo', email='elena.castillo@uni.edu')>, <Estudiante(id=6, nombre='Fernando López', email='fernando.lopez@uni.edu')>, <Estudiante(id=7, nombre='Gabriela Torres', email='gabriela.torres@uni.edu')>, <Estudiante(id=8, nombre='Hugo Sánchez', email='hugo.sanchez@uni.edu')>, <Estudiante(id=9, nombre='Isabel Vega', email='isabel.vega@uni.edu')>, <Estudiante(id=10, nombre='Javier Ortiz', email='javier.ortiz@uni.edu')>, <Estudiante(id=11, nombre='Karen Morales',..................
```

Significa que todo funciona correctamente!


Para sincronizar tus tablas con el ORM usa el siguiente script:

```bash
python correction_tables.py
```

Luego vete a la documentación del frontend [FRONTEND DOCUMENTATION](https://github.com/CarEsteban/lab3-steamlit/tree/main/frontend) para saber como iniciar el frontend