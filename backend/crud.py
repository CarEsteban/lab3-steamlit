from sqlalchemy.orm import Session
from models import (
    Estudiante,
    Curso,
    Profesor,
    Inscripcion,
    Asignacion,
    EnrollmentStatus
)
from datetime import date

# ---------- Estudiante CRUD ----------
def create_estudiante(db: Session, nombre: str, email: str, fecha_nacimiento: date) -> Estudiante:
    est = Estudiante(nombre=nombre, email=email, fecha_nacimiento=fecha_nacimiento)
    db.add(est)
    db.commit()
    db.refresh(est)
    return est

def get_estudiante(db: Session, est_id: int) -> Estudiante | None:
    return db.query(Estudiante).filter(Estudiante.id == est_id).first()

def list_estudiantes(db: Session, skip: int = 0, limit: int = 100) -> list[Estudiante]:
    return db.query(Estudiante).offset(skip).limit(limit).all()

def update_estudiante(db: Session, est_id: int, **kwargs) -> Estudiante | None:
    est = db.query(Estudiante).get(est_id)
    if not est:
        return None
    for key, val in kwargs.items():
        setattr(est, key, val)
    db.commit()
    db.refresh(est)
    return est

def delete_estudiante(db: Session, est_id: int) -> bool:
    est = db.query(Estudiante).get(est_id)
    if not est:
        return False
    db.delete(est)
    db.commit()
    return True

# ---------- Curso CRUD ----------
def create_curso(db: Session, codigo: str, nombre: str, descripcion: str | None = None) -> Curso:
    cur = Curso(codigo=codigo, nombre=nombre, descripcion=descripcion)
    db.add(cur)
    db.commit()
    db.refresh(cur)
    return cur

def get_curso(db: Session, curso_id: int) -> Curso | None:
    return db.query(Curso).filter(Curso.id == curso_id).first()

def list_cursos(db: Session, skip: int = 0, limit: int = 100) -> list[Curso]:
    return db.query(Curso).offset(skip).limit(limit).all()

def update_curso(db: Session, curso_id: int, **kwargs) -> Curso | None:
    cur = db.query(Curso).get(curso_id)
    if not cur:
        return None
    for key, val in kwargs.items():
        setattr(cur, key, val)
    db.commit()
    db.refresh(cur)
    return cur

def delete_curso(db: Session, curso_id: int) -> bool:
    cur = db.query(Curso).get(curso_id)
    if not cur:
        return False
    db.delete(cur)
    db.commit()
    return True

# ---------- Profesor CRUD ----------
def create_profesor(db: Session, nombre: str, email: str) -> Profesor:
    prof = Profesor(nombre=nombre, email=email)
    db.add(prof)
    db.commit()
    db.refresh(prof)
    return prof

def get_profesor(db: Session, profesor_id: int) -> Profesor | None:
    return db.query(Profesor).filter(Profesor.id == profesor_id).first()

def list_profesores(db: Session, skip: int = 0, limit: int = 100) -> list[Profesor]:
    return db.query(Profesor).offset(skip).limit(limit).all()

def update_profesor(db: Session, profesor_id: int, **kwargs) -> Profesor | None:
    prof = db.query(Profesor).get(profesor_id)
    if not prof:
        return None
    for key, val in kwargs.items():
        setattr(prof, key, val)
    db.commit()
    db.refresh(prof)
    return prof

def delete_profesor(db: Session, profesor_id: int) -> bool:
    prof = db.query(Profesor).get(profesor_id)
    if not prof:
        return False
    db.delete(prof)
    db.commit()
    return True

# ---------- Inscripcion CRUD ----------
def create_inscripcion(db: Session, estudiante_id: int, curso_id: int,
                        estado: EnrollmentStatus, fecha_inscripcion: date) -> Inscripcion:
    ins = Inscripcion(
        estudiante_id=estudiante_id,
        curso_id=curso_id,
        estado=estado,
        fecha_inscripcion=fecha_inscripcion
    )
    db.add(ins)
    db.commit()
    db.refresh(ins)
    return ins

def get_inscripcion(db: Session, ins_id: int) -> Inscripcion | None:
    return db.query(Inscripcion).filter(Inscripcion.id == ins_id).first()

def list_inscripciones(db: Session, skip: int = 0, limit: int = 100) -> list[Inscripcion]:
    return db.query(Inscripcion).offset(skip).limit(limit).all()

def update_inscripcion(db: Session, ins_id: int, **kwargs) -> Inscripcion | None:
    ins = db.query(Inscripcion).get(ins_id)
    if not ins:
        return None
    for key, val in kwargs.items():
        setattr(ins, key, val)
    db.commit()
    db.refresh(ins)
    return ins

def delete_inscripcion(db: Session, ins_id: int) -> bool:
    ins = db.query(Inscripcion).get(ins_id)
    if not ins:
        return False
    db.delete(ins)
    db.commit()
    return True

# ---------- Asignacion CRUD ----------
def create_asignacion(db: Session, curso_id: int, profesor_id: int) -> Asignacion:
    asign = Asignacion(curso_id=curso_id, profesor_id=profesor_id)
    db.add(asign)
    db.commit()
    db.refresh(asign)
    return asign

def get_asignacion(db: Session, asign_id: int) -> Asignacion | None:
    return db.query(Asignacion).filter(Asignacion.id == asign_id).first()

def list_asignaciones(db: Session, skip: int = 0, limit: int = 100) -> list[Asignacion]:
    return db.query(Asignacion).offset(skip).limit(limit).all()

def delete_asignacion(db: Session, asign_id: int) -> bool:
    asign = db.query(Asignacion).get(asign_id)
    if not asign:
        return False
    db.delete(asign)
    db.commit()
    return True
