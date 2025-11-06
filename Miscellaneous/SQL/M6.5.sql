USE dummydb;
SELECT * FROM employees;

/*
Determine the third highest salary and which employee receives it?
*/
SELECT CONCAT(first_name, ' ', last_name) AS Name, salary AS Salary 
FROM employees 
WHERE salary = (
SELECT MAX(salary)
FROM employees WHERE salary < (
SELECT MAX(salary) 
FROM employees WHERE salary < (
SELECT MAX(salary)
FROM employees)));

/*
Determine the third lowest salary and which employee receives it?
*/
SELECT CONCAT(first_name, ' ', last_name) AS Name, salary as Salary 
FROM employees
WHERE salary = (
SELECT MIN(salary)
FROM employees WHERE salary > (
SELECT MIN(salary)
FROM employees WHERE salary > (
SELECT MIN(salary) FROM employees
)));

/*
Which employee has been hired after Steven?
*/

SELECT CONCAT(first_name, ' ', last_name) AS Name, hire_date
FROM employees
WHERE hire_date = (
SELECT MIN(hire_date) 
FROM employees
WHERE hire_date > (
SELECT hire_date
FROM employees
 WHERE first_name = 'Steven' AND last_name = 'King'
));

/*
With common table expression solve the question 1 and 2
*/