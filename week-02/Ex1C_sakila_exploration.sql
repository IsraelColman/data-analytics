/*
a) actor id, first name, last name, and last update. 
b) film id, title, description, release year, language id, original language id, rental duration, rental rate, length, replacement cost, rating, special features, last update.
c) film_actor. 
d) the table includes the fields rental id, rental date, inventory id, customer id, return date, staff id, and last update. the table is easy read because of the format. it reminds me of an excel sheet.
e) inventory id, film id, store id, and last updates.
f) I would say film, inventory, and rental are the tables you need. You can look at the rental table and find the inventory id, you can then find that inventory id in the inventory table. after finding the inventory
id on the inventory table, you can see which film id is connected to that inventory id. from there you can look at the film table and find that film id which then shows you the name of that film.   
*/

select inventory_id, rental_date from rental;
select inventory_id, film_id from inventory;
select film_id, title from film;