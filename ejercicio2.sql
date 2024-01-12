"""1. Crea una base de datos llamada "MiBaseDeDatos"."""

He ido a databases - boton derecho -crear- database y he puesto el nombre.

"""22. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero)."""
CREATE TABLE IF NOT EXISTS Usuarios(
	id INT PRIMARY KEY,
	nombre VARCHAR (255),
	edad INT
);


"""3. Inserta dos registros en la tabla "Usuarios"."""

INSERT INTO Usuarios(id,nombre,edad)
VALUES (1,'juan', 25);

INSERT INTO Usuarios(id,nombre,edad)
VALUES (2,'ana', 30);

"""4. Actualiza la edad de un usuario en la tabla "Usuarios"."""
UPDATE usuarios
SET edad = 28
WHERE id = 1;

UPDATE usuarios
SET edad = 31
WHERE id = 2;
"""5. Elimina un usuario de la tabla "Usuarios"."""
DELETE FROM usuarios
WHERE id = 1;

"""Nivel de dificultad: Moderado
1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto)."""
CREATE TABLE ciudades(
	id INT PRIMARY KEY,
	nombre VARCHAR(255),
	pais VARCHAR(255)
);

"""2. Inserta al menos tres registros en la tabla "Ciudades"."""
INSERT INTO ciudades(id,nombre,pais)
VALUES 
(1,'Madrid','España'),
(2,'Lisboa', 'Portugal'),
(3,'Paris','Francia');

"""3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id"
de la tabla "Ciudades"."""

ALTER TABLE usuarios 
	ADD CONSTRAINT FK_usuarios FOREIGN KEY(id)
	REFERENCES ciudades (id)


"""4. Realiza una consulta que muestre los nombres de los usuarios junto con el
nombre de su ciudad y país (utiliza un LEFT JOIN)."""

SELECT usuarios.nombre, ciudades.nombre, ciudades.pais
FROM usuarios
LEFT JOIN ciudades
ON usuarios.id = ciudades.id;

"""5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad
asociada (utiliza un INNER JOIN)"""

SELECT usuarios.nombre, ciudades.nombre
FROM usuarios
INNER JOIN ciudades
ON usuarios.id = ciudades.id;