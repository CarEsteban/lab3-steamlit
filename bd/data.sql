-- ================================
-- 2.1 Estudiantes (50)
-- ================================
INSERT INTO estudiante (nombre, email, fecha_nacimiento) VALUES
('Ana Gómez',          'ana.gomez@uni.edu',          '1997-01-15'),
('Bruno Martínez',     'bruno.martinez@uni.edu',     '1997-02-14'),
('Carla Ruiz',         'carla.ruiz@uni.edu',         '1997-03-16'),
('Diego Fernández',    'diego.fernandez@uni.edu',    '1997-04-15'),
('Elena Castillo',     'elena.castillo@uni.edu',     '1997-05-15'),
('Fernando López',     'fernando.lopez@uni.edu',     '1997-06-14'),
('Gabriela Torres',    'gabriela.torres@uni.edu',    '1997-07-14'),
('Hugo Sánchez',       'hugo.sanchez@uni.edu',       '1997-08-13'),
('Isabel Vega',        'isabel.vega@uni.edu',        '1997-09-12'),
('Javier Ortiz',       'javier.ortiz@uni.edu',       '1997-10-12'),
('Karen Morales',      'karen.morales@uni.edu',      '1997-11-11'),
('Luis Ramírez',       'luis.ramirez@uni.edu',       '1997-12-11'),
('María Hernández',    'maria.hernandez@uni.edu',    '1998-01-10'),
('Nicolás Pérez',      'nicolas.perez@uni.edu',      '1998-02-09'),
('Óscar Díaz',         'oscar.diaz@uni.edu',         '1998-03-11'),
('Paula Jiménez',      'paula.jimenez@uni.edu',      '1998-04-10'),
('Ricardo Silva',      'ricardo.silva@uni.edu',      '1998-05-10'),
('Sandra López',       'sandra.lopez@uni.edu',       '1998-06-09'),
('Tomás Martínez',     'tomas.martinez@uni.edu',     '1998-07-09'),
('Valeria Ruiz',       'valeria.ruiz@uni.edu',       '1998-08-08'),
('Andrés Blanco',      'andres.blanco@uni.edu',      '1998-09-07'),
('Beatriz Navarro',    'beatriz.navarro@uni.edu',    '1998-10-07'),
('Carlos Medina',      'carlos.medina@uni.edu',      '1998-11-06'),
('Daniela Castillo',   'daniela.castillo@uni.edu',   '1998-12-06'),
('Eduardo Vega',       'eduardo.vega@uni.edu',       '1999-01-05'),
('Fernanda Rojas',     'fernanda.rojas@uni.edu',     '1999-02-04'),
('Gustavo Paredes',    'gustavo.paredes@uni.edu',    '1999-03-06'),
('Helena Cruz',        'helena.cruz@uni.edu',        '1999-04-05'),
('Ignacio Bravo',      'ignacio.bravo@uni.edu',      '1999-05-05'),
('Julia León',         'julia.leon@uni.edu',         '1999-06-04'),
('Kevin Herrera',      'kevin.herrera@uni.edu',      '1999-07-04'),
('Lucía Ramos',        'lucia.ramos@uni.edu',        '1999-08-03'),
('Manuel Ortiz',       'manuel.ortiz@uni.edu',       '1999-09-02'),
('Natalia Ponce',      'natalia.ponce@uni.edu',      '1999-10-02'),
('Patricia Molina',    'patricia.molina@uni.edu',    '1999-11-01'),
('Quetzal Mayorga',    'quetzal.mayorga@uni.edu',    '1999-12-01'),
('Raúl Cabrera',       'raul.cabrera@uni.edu',       '2000-01-31'),
('Sofía Guzmán',       'sofia.guzman@uni.edu',       '2000-02-29'),
('Usuario Ramos',      'usuario.ramos@uni.edu',      '2000-03-30'),
('Victoria Solís',     'victoria.solis@uni.edu',     '2000-04-29'),
('Walter Acosta',      'walter.acosta@uni.edu',      '2000-05-29'),
('Ximena Fuentes',     'ximena.fuentes@uni.edu',     '2000-06-28'),
('Yolanda Peña',       'yolanda.pena@uni.edu',       '2000-07-28'),
('Zacarías Vargas',    'zacarias.vargas@uni.edu',    '2000-08-27'),
('Adriana Serrano',    'adriana.serrano@uni.edu',    '2000-09-26'),
('Benjamín Cruz',      'benjamin.cruz@uni.edu',      '2000-10-26'),
('Clara Castro',       'clara.castro@uni.edu',       '2000-11-25'),
('David Blanco',       'david.blanco@uni.edu',       '2000-12-25'),
('Eva Navarro',        'eva.navarro@uni.edu',        '2001-01-24'),
('Federico Díaz',      'federico.diaz@uni.edu',      '2001-02-23')
;

-- ================================
-- 2.2 Cursos (12)
-- ================================
INSERT INTO curso (codigo, nombre, descripcion) VALUES
('MAT101',  'Cálculo I',            'Funciones, límites y derivadas'),
('PHY202',  'Física II',            'Electricidad y magnetismo'),
('DAT303',  'Estructuras de Datos', 'Listas, árboles y grafos'),   -- DAT303 cumple 3L+3D
('ENG104',  'Inglés Técnico',       'Inglés para ingeniería'),
('HIS210',  'Historia Moderna',     'Europa y América en el siglo XX'),
('BIO150',  'Biología Celular',     'Estructura y función celular'),
('CHE111',  'Química General',      'Estequiometría y termodinámica'),
('ART305',  'Diseño Gráfico',       'Principios de diseño y Adobe'),
('ECO220',  'Microeconomía',        'Teoría y aplicaciones prácticas'),
('PSY330',  'Psicología Social',    'Comportamiento humano en grupo'),
('PHI101',  'Filosofía I',          'Grandes pensadores y conceptos básicos'),
('ART210',  'Historia del Arte',    'Arte renacentista, barroco y moderno')
;

-- ================================
-- 2.3 Profesores (10)
-- ================================
INSERT INTO profesor (nombre, email) VALUES
('Dr. Luis Herrera',      'luis.herrera@uni.edu'),
('Dra. María Peña',       'maria.pena@uni.edu'),
('Ing. Ricardo Morales',  'ricardo.morales@uni.edu'),
('Lic. Patricia Vega',    'patricia.vega@uni.edu'),
('Prof. Andrés Quintana', 'andres.quintana@uni.edu'),
('Dra. Sofía Ramírez',    'sofia.ramirez@uni.edu'),
('Mtro. Carlos Castillo', 'carlos.castillo@uni.edu'),
('Lic. Andrea Blanco',    'andrea.blanco@uni.edu'),
('Dr. Juan Soto',         'juan.soto@uni.edu'),
('Dra. Clara Flores',     'clara.flores@uni.edu')
;

-- ================================
-- 2.4 Asignaciones (36 cruces, 12 cursos × 3 profesores)
-- ================================
INSERT INTO asignacion (curso_id, profesor_id) VALUES
( 1,  1), ( 1,  2), ( 1,  3),  -- MAT101
( 2,  3), ( 2,  4), ( 2,  5),  -- PHY202
( 3,  5), ( 3,  6), ( 3,  7),  -- DAT303
( 4,  7), ( 4,  8), ( 4,  9),  -- ENG104
( 5,  2), ( 5,  9), ( 5, 10),  -- HIS210
( 6,  6), ( 6, 10), ( 6,  1),  -- BIO150
( 7,  1), ( 7,  3), ( 7,  5),  -- CHE111
( 8,  5), ( 8,  7), ( 8,  8),  -- ART305
( 9,  8), ( 9, 10), ( 9,  2),  -- ECO220
(10,  9), (10,  4), (10,  6),  -- PSY330
(11,  2), (11,  6), (11,  9),  -- PHI101
(12,  3), (12,  5), (12, 10)   -- ART210
;

-- ================================
-- 2.5 Inscripciones (100 cruces)
-- ================================
INSERT INTO inscripcion (estudiante_id, curso_id, estado, fecha_inscripcion) VALUES
( 1,  1, 'active',    '2025-01-15'),
( 1,  3, 'completed', '2025-02-10'),
( 1,  5, 'dropped',   '2025-03-04'),
( 1,  7, 'active',    '2025-04-02'),
( 1, 10, 'completed', '2025-05-01'),
( 2,  2, 'active',    '2025-01-16'),
( 2,  4, 'completed', '2025-02-11'),
( 2,  6, 'dropped',   '2025-03-05'),
( 2,  8, 'active',    '2025-04-03'),
( 2, 12, 'completed', '2025-05-02'),
( 3,  3, 'active',    '2025-01-17'),
( 3,  5, 'completed', '2025-02-12'),
( 3,  7, 'dropped',   '2025-03-06'),
( 3,  9, 'active',    '2025-04-04'),
( 3, 11, 'completed', '2025-05-03'),
( 4,  4, 'active',    '2025-01-18'),
( 4,  6, 'completed', '2025-02-13'),
( 4,  8, 'dropped',   '2025-03-07'),
( 4, 10, 'active',    '2025-04-05'),
( 4, 12, 'completed', '2025-05-04'),
( 5,  5, 'active',    '2025-01-19'),
( 5,  7, 'completed', '2025-02-14'),
( 5,  9, 'dropped',   '2025-03-08'),
( 5, 11, 'active',    '2025-04-06'),
( 5,  1, 'completed', '2025-05-05'),
( 6,  6, 'active',    '2025-01-20'),
( 6,  8, 'completed', '2025-02-15'),
( 6, 10, 'dropped',   '2025-03-09'),
( 6, 12, 'active',    '2025-04-07'),
( 6,  2, 'completed', '2025-05-06'),
( 7,  7, 'active',    '2025-01-21'),
( 7,  9, 'completed', '2025-02-16'),
( 7, 11, 'dropped',   '2025-03-10'),
( 7,  1, 'active',    '2025-04-08'),
( 7,  3, 'completed', '2025-05-07'),
( 8,  8, 'active',    '2025-01-22'),
( 8, 10, 'completed', '2025-02-17'),
( 8, 12, 'dropped',   '2025-03-11'),
( 8,  2, 'active',    '2025-04-09'),
( 8,  4, 'completed', '2025-05-08'),
( 9,  9, 'active',    '2025-01-23'),
( 9, 11, 'completed', '2025-02-18'),
( 9,  1, 'dropped',   '2025-03-12'),
( 9,  3, 'active',    '2025-04-10'),
( 9,  5, 'completed', '2025-05-09'),
(10, 10, 'active',    '2025-01-24'),
(10, 12, 'completed', '2025-02-19'),
(10,  2, 'dropped',   '2025-03-13'),
(10,  4, 'active',    '2025-04-11'),
(10,  6, 'completed', '2025-05-10'),
(11, 11, 'active',    '2025-01-25'),
(11,  1, 'completed', '2025-02-20'),
(11,  3, 'dropped',   '2025-03-14'),
(11,  5, 'active',    '2025-04-12'),
(11,  7, 'completed', '2025-05-11'),
(12, 12, 'active',    '2025-01-26'),
(12,  2, 'completed', '2025-02-21'),
(12,  4, 'dropped',   '2025-03-15'),
(12,  6, 'active',    '2025-04-13'),
(12,  8, 'completed', '2025-05-12'),
(13,  1, 'active',    '2025-01-27'),
(13,  3, 'completed', '2025-02-22'),
(13,  5, 'dropped',   '2025-03-16'),
(13,  7, 'active',    '2025-04-14'),
(13,  9, 'completed', '2025-05-13'),
(14, 10, 'active',    '2025-01-28'),
(14, 12, 'completed', '2025-02-23'),
(14,  2, 'dropped',   '2025-03-17'),
(14,  4, 'active',    '2025-04-15'),
(14,  6, 'completed', '2025-05-14'),
(15, 11, 'active',    '2025-01-29'),
(15,  1, 'completed', '2025-02-24'),
(15,  3, 'dropped',   '2025-03-18'),
(15,  5, 'active',    '2025-04-16'),
(15,  7, 'completed', '2025-05-15')
;
