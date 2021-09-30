/
 ---- crear una tabla -----

create table customers(
id int primary key not null,
firstname varchar(50) not null,
lastname varchar(50) not null,
address varchar(100),
city varchar(50)
);

*/

--Consultar informacion de una tabla
--SELECT *-> extraer toda la informacion
select * from customers c ;

-- INSERT campos desde tabla -> insertar valores
INSERT into customers(id, firstname, lastname, address, city) 
values(1, "Fabian Guillermo", "Diaz Bernal", "Cll 7 # 9-29", "San Gil");

*/
--guardando con ID NULLO

--insert into customers (id, firstname , lastname, address, city)
--values(2, "juan", "perea", null, "medellin");
*/

--Eliminar un registro
--DELETE FROM customers WHERE id = 2;

--Actualizar una columna
--UPDATE customers set address = "cll 10 # 7-42"
--WHERE id  = 2;

--Eliminar tabla customers
DROP table customers;