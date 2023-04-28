# Write your MySQL query statement below

SELECT t2.product_name, t1.year, t1.price FROM Sales as t1
LEFT JOIN Product as t2
ON t2.product_id = t1.product_id;