create type enrollment_status as enum('active', 'completed', 'dropped');

create domain course_code as text check (value ~ '^[A-Z]{3}[0-9]{3}$');

create table if not exists estudiante (
  id bigint primary key generated always as identity,
  nombre text not null,
  email text unique not null,
  fecha_nacimiento date not null
);

create table if not exists  curso (
  id bigint primary key generated always as identity,
  codigo course_code not null unique,
  nombre text not null,
  descripcion text
);

create table if not exists profesor (
  id bigint primary key generated always as identity,
  nombre text not null,
  email text unique not null
);

create table if not exists  inscripcion (
  id bigint primary key generated always as identity,
  estudiante_id bigint not null references estudiante (id) on delete cascade,
  curso_id bigint not null references curso (id) on delete cascade,
  estado enrollment_status not null,
  fecha_inscripcion date not null default current_date,
  unique (estudiante_id, curso_id)
);

create table if not exists  asignacion (
  id bigint primary key generated always as identity,
  curso_id bigint not null references curso (id) on delete cascade,
  profesor_id bigint not null references profesor (id) on delete cascade,
  unique (curso_id, profesor_id)
);

create view v_course_enrollment as
select
  e.id as estudiante_id,
  e.nombre as estudiante_nombre,
  c.id as curso_id,
  c.nombre as curso_nombre,
  i.estado
from
  estudiante e
  join inscripcion i on e.id = i.estudiante_id
  join curso c on i.curso_id = c.id;

create view v_course_teachers as
select
  c.id as curso_id,
  c.nombre as curso_nombre,
  p.id as profesor_id,
  p.nombre as profesor_nombre
from
  curso c
  join asignacion a on c.id = a.curso_id
  join profesor p on a.profesor_id = p.id;