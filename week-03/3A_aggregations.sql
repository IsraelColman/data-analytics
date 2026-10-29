USE northwind;

-- 1. Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price.

SELECT MIN(UnitPrice) CheapestItem
FROM products;

SELECT ProductName, UnitPrice
FROM products
ORDER BY UnitPrice
LIMIT 1;


-- 2. Write a query to find the average price of all items that Northwind sells.
-- (Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
-- using the ROUND function to round the average price to the nearest cent.)

SELECT ProductName,
ROUND(AVG(UnitPrice), 2) AvgPrice
FROM products
GROUP BY ProductName
ORDER BY AvgPrice DESC, ProductName;


-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.

SELECT MAX(UnitPrice) MostExpensiveItem
FROM products;

SELECT p.ProductName, s.CompanyName SupplierName,
p.UnitPrice MostExpensiveItem
FROM products p
INNER JOIN suppliers s
ON p.SupplierID = s.SupplierID
ORDER BY p.UnitPrice DESC
LIMIT 1;

SELECT p.ProductName, s.CompanyName SupplierName,
MAX(p.UnitPrice) MostExpensiveItem
FROM products p
INNER JOIN suppliers s
ON p.SupplierID = s.SupplierID
GROUP BY p.ProductName, s.CompanyName
LIMIT 1;


-- 4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
-- salaries).

SELECT SUM(Salary) MonthlySalary
FROM employees;


-- 5. Write a query to identify the highest salary and the lowest salary amounts which any
-- employee makes. (Just the amounts, not the specific employees!)

SELECT MAX(Salary) HighestSalary,
MIN(Salary) LowestSalary
FROM employees;


-- 6. Write a query to find the name and supplier ID of each supplier and the number of
-- items they supply. Hint: Join is your friend here.

SELECT s.SupplierID, s.CompanyName SupplierName,
COUNT(*) SuppliedItems
FROM suppliers s
INNER JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;


-- 7. Write a query to find the list of all category names and the average price for items in
-- each category.

SELECT c.CategoryName,
ROUND(AVG(p.UnitPrice), 2) AvgPrice
FROM categories c
INNER JOIN products p
ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName;


-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply.

SELECT s.CompanyName SupplierName, s.SupplierID,
COUNT(p.ProductID) NumberOfItems
FROM suppliers s 
INNER JOIN products p 
ON p.SupplierID = s.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING NumberOfItems >= 5; 


-- 9. Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list.

SELECT ProductID, ProductName,
ROUND(UnitPrice * UnitsInStock, 2) InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName;