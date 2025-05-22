from sqlalchemy import (
    Column, BigInteger, Text, Date, Enum, CheckConstraint,
    ForeignKey, UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum

Base = declarative_base()

# 1) Tipo personalizado: enrollment_status
class EnrollmentStatus(enum.Enum):
    active = "active"
    completed = "completed"
    dropped = "dropped"

class Estudiante(Base):
    __tablename__ = "estudiante"
    id               = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre           = Column(Text, nullable=False)
    email            = Column(Text, unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)

    inscripciones = relationship("Inscripcion", back_populates="estudiante")

    def __repr__(self):
        return f"<Estudiante(id={self.id}, nombre={self.nombre!r}, email={self.email!r})>"

class Curso(Base):
    __tablename__ = "curso"
    id          = Column(BigInteger, primary_key=True, autoincrement=True)
    codigo      = Column(Text, nullable=False, unique=True)  # DOMAIN aplicado en DB
    nombre      = Column(Text, nullable=False)
    descripcion = Column(Text)

    __table_args__ = (
        CheckConstraint("codigo ~ '^[A-Z]{3}[0-9]{3}$'", name="course_code_check"),
    )

    inscripciones = relationship("Inscripcion", back_populates="curso")
    asignaciones  = relationship("Asignacion", back_populates="curso")

    def __repr__(self):
        return f"<Curso(id={self.id}, codigo={self.codigo!r}, nombre={self.nombre!r})>"

class Profesor(Base):
    __tablename__ = "profesor"
    id     = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(Text, nullable=False)
    email  = Column(Text, unique=True, nullable=False)

    asignaciones = relationship("Asignacion", back_populates="profesor")

    def __repr__(self):
        return f"<Profesor(id={self.id}, nombre={self.nombre!r}, email={self.email!r})>"

class Inscripcion(Base):
    __tablename__ = "inscripcion"
    id                 = Column(BigInteger, primary_key=True, autoincrement=True)
    estudiante_id      = Column(BigInteger, ForeignKey("estudiante.id", ondelete="CASCADE"), nullable=False)
    curso_id           = Column(BigInteger, ForeignKey("curso.id",      ondelete="CASCADE"), nullable=False)
    estado             = Column(Enum(EnrollmentStatus), nullable=False)
    fecha_inscripcion  = Column(Date, nullable=False)

    __table_args__ = (
        UniqueConstraint("estudiante_id", "curso_id", name="uix_est_curso"),
    )

    estudiante = relationship("Estudiante", back_populates="inscripciones")
    curso      = relationship("Curso",      back_populates="inscripciones")

    def __repr__(self):
        return (
            f"<Inscripcion(id={self.id}, estudiante_id={self.estudiante_id}, "
            f"curso_id={self.curso_id}, estado={self.estado.value!r}, "
            f"fecha_inscripcion={self.fecha_inscripcion})>"
        )

class Asignacion(Base):
    __tablename__ = "asignacion"
    id          = Column(BigInteger, primary_key=True, autoincrement=True)
    curso_id    = Column(BigInteger, ForeignKey("curso.id",    ondelete="CASCADE"), nullable=False)
    profesor_id = Column(BigInteger, ForeignKey("profesor.id", ondelete="CASCADE"), nullable=False)

    __table_args__ = (
        UniqueConstraint("curso_id", "profesor_id", name="uix_curso_profesor"),
    )

    curso    = relationship("Curso",    back_populates="asignaciones")
    profesor = relationship("Profesor", back_populates="asignaciones")

    def __repr__(self):
        return f"<Asignacion(id={self.id}, curso_id={self.curso_id}, profesor_id={self.profesor_id})>"
