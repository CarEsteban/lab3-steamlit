# backend/test_crud.py

from datetime import date
from db import get_session, engine
from models import Base, EnrollmentStatus
from crud import (
    create_estudiante, get_estudiante, list_estudiantes, update_estudiante, delete_estudiante,
    create_curso, get_curso, list_cursos, update_curso, delete_curso,
    create_profesor, get_profesor, list_profesores, update_profesor, delete_profesor,
    create_inscripcion, get_inscripcion, list_inscripciones, update_inscripcion, delete_inscripcion,
    create_asignacion, get_asignacion, list_asignaciones, delete_asignacion
)
from sqlalchemy import text

def test_estudiante(db):
    print("\n--- Test Estudiante CRUD ---")
    e = create_estudiante(db, "Test User", "pruebatest@uvg.edu.gt", date(1990,1,1))
    print("CREATE:", e)
    print("READ: ", get_estudiante(db, e.id))
    print("LIST:", list_estudiantes(db))
    print("UPDATE:", update_estudiante(db, e.id, nombre="Updated User"))
    print("DELETE:", delete_estudiante(db, e.id))
    assert get_estudiante(db, e.id) is None

def test_curso(db):
    print("\n--- Test Curso CRUD ---")
    c = create_curso(db, "ABS133", "Curso Alfa", "Descripción")
    print("CREATE:", c)
    print("READ: ", get_curso(db, c.id))
    print("LIST:", list_cursos(db))
    print("UPDATE:", update_curso(db, c.id, nombre="Curso Beta", descripcion="Desc upd"))
    print("DELETE:", delete_curso(db, c.id))
    assert get_curso(db, c.id) is None

def test_profesor(db):
    print("\n--- Test Profesor CRUD ---")
    p = create_profesor(db, "Prof Test Test", "prof@uvg.edu.gt")
    print("CREATE:", p)
    print("READ: ", get_profesor(db, p.id))
    print("LIST:", list_profesores(db))
    print("UPDATE:", update_profesor(db, p.id, nombre="Prof Updated"))
    print("DELETE:", delete_profesor(db, p.id))
    assert get_profesor(db, p.id) is None

def test_inscripcion(db):
    print("\n--- Test Inscripcion CRUD ---")
    # Primero crea un estudiante y un curso
    e = create_estudiante(db, "Inscr User", "inscripcion@uvg.edu.gt", date(1991,2,2))
    c = create_curso(db, "DEF456", "Curso Gamma", "Desc ins")
    i = create_inscripcion(db, e.id, c.id, EnrollmentStatus.active, date.today())
    print("CREATE:", i)
    print("READ: ", get_inscripcion(db, i.id))
    print("LIST:", list_inscripciones(db))
    print("UPDATE:", update_inscripcion(db, i.id, estado=EnrollmentStatus.completed))
    print("DELETE:", delete_inscripcion(db, i.id))
    assert get_inscripcion(db, i.id) is None
    # Limpia estudiante y curso usados
    delete_estudiante(db, e.id)
    delete_curso(db, c.id)

def test_asignacion(db):
    print("\n--- Test Asignacion CRUD ---")
    # Primero crea un curso y un profesor
    c = create_curso(db, "GHI789", "Curso Delta", "Desc asig")
    p = create_profesor(db, "Asig Prof", "asignacion@uvg.edu.gt")
    a = create_asignacion(db, c.id, p.id)
    print("CREATE:", a)
    print("READ: ", get_asignacion(db, a.id))
    print("LIST:", list_asignaciones(db))
    print("DELETE:", delete_asignacion(db, a.id))
    assert get_asignacion(db, a.id) is None
    # Limpia curso y profesor usados
    delete_curso(db, c.id)
    delete_profesor(db, p.id)


if __name__ == "__main__":
    db = get_session()

    test_estudiante(db)
    test_curso(db)
    test_profesor(db)
    test_inscripcion(db)
    test_asignacion(db)

    print("\n🎉 Todos los tests CRUD pasaron correctamente.")
