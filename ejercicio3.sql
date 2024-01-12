"""Ejercicios 3
1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico)."""

CREATE TABLE productos(
	id INT PRIMARY KEY,
	nombre VARCHAR(255),
	precio NUMERIC 
);

"""2. Inserta al menos cinco registros en la tabla "Productos"."""

INSERT INTO productos (id,nombre,precio)
VALUES
(1,'camiseta',15),
(2,'pantalon',30),
(3,'gorra',25),
(4,'gafas',80),
(5,'calcetines',9);

"""3. Actualiza el precio de un producto en la tabla "Productos"."""

UPDATE productos 
SET precio = 20
WHERE id = 1;


"""4. Elimina un producto de la tabla "Productos"."""
DELETE FROM productos 
WHERE id = 2;

"""5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos")."""

SELECT usuarios.nombre, productos.nombre
FROM productos
INNER JOIN usuarios ON usuarios.id = productos.id

