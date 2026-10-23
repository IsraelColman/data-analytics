/* 
1. 
a) The name of the table is products.
b) The table name is categories.
*/

USE northwind;
SELECT * FROM employees;
/* 
9 records were returned. 
there is a pulldown window where you can change the amount of rows you want to limit.
*/

SELECT * FROM categories; -- the category id of seafood is 8.

SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders;