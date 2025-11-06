USE DUMMYDB;

SELECT * FROM EMPLOYEES;

SELECT e1.first_name, e1.manager_id
FROM employees e1
	JOIN employees e2 ON e1.manager_id = e2.manager_id
	WHERE e1.employee_id != e2.employee_id;

CREATE DATABASE M8_Assignment;

USE M8_Assignment;

CREATE TABLE Employees (
    Employee_Id INT PRIMARY KEY,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Date_Of_Birth DATE,
    Department_Id INT,
    Salary DECIMAL(10, 2)
);

CREATE TABLE Projects (
    Project_Id INT PRIMARY KEY,
    Project_Name VARCHAR(100),
    Start_Date DATE,
    End_Date DATE,
    Budget DECIMAL(12, 2)
);

CREATE TABLE Employee_Projects (
    Employee_Id INT,
    Project_Id INT,
    PRIMARY KEY (Employee_Id, Project_Id),
    FOREIGN KEY (Employee_Id) REFERENCES Employees(Employee_Id),
    FOREIGN KEY (Project_Id) REFERENCES Projects(Project_Id)
);

USE dummydb;

SELECT salary 
FROM employees 
WHERE salary = (
SELECT MAX(salary) FROM employees WHERE salary < (
SELECT MAX(salary) FROM employees WHERE salary <(
SELECT MAX(salary) FROM employees WHERE salary
)));

SELECT * FROM departments;
SELECT * FROM employees;

SELECT d.department_name AS Department, COUNT(e.employee_id) AS Employees
FROM departments AS d
	JOIN employees AS e ON d.department_id = e.department_id
	GROUP BY d.department_name;
    
SELECT CONCAT(e.first_name, ' ', e.last_name) AS Name, d.department_name AS Department
FROM employees AS e
	INNER JOIN departments AS d
			ON e.department_id = d.department_id;
            
SELECT CONCAT(e.first_name, ' ', e.last_name) AS Name, d.department_name AS Department
FROM employees AS e
	LEFT JOIN departments AS d
			ON e.department_id = d.department_id;
            
SELECT CONCAT(e.first_name, ' ', e.last_name) AS Name, d.department_name AS Department
FROM employees AS e
	RIGHT JOIN departments AS d
			ON e.department_id = d.department_id;
            
SELECT CONCAT(e.first_name, ' ', e.last_name) AS Name, d.department_name AS Department
FROM employees AS e
	CROSS JOIN departments AS d;
    
WITH avgSalary AS (
SELECT AVG(salary) AS avgS
FROM employees)

SELECT CONCAT(first_name, ' ', last_name) AS name, salary
FROM employees, avgSalary
WHERE salary > avgSalary.avgS;

WITH steve AS (
SELECT salary AS steveS
FROM employees
WHERE first_name = 'Steven' AND last_name = 'King')

SELECT CONCAT(first_name, ' ', last_name) AS Name
FROM employees, steve
WHERE employees.salary < steve.steveS;

SELECT d.department_name AS Department, CONCAT(e.first_name, ' ', e.last_name) AS Name
FROM departments AS d
	JOIN employees AS e 
    ON d.manager_id = e.employee_id;
    
SELECT * FROM departments;
SELECT * FROM locations;

SELECT department_name AS DEPARTMENT, city AS CITY
FROM departments
	JOIN locations
    USING(location_id)