# Write your MySQL query statement below

SELECT t2.unique_id, t1.name FROM Employees as t1
LEFT JOIN EmployeeUni as t2
ON t2.id = t1.id;