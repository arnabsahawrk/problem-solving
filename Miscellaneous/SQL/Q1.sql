USE employee;

DROP TABLE employees;

CREATE TABLE employee(
  EmpId INT AUTO_INCREMENT PRIMARY KEY,
  EmpName VARCHAR(50) NOT NULL,
  JoiningYear INT NOT NULL,
  Birthday DATE NOT NULL,
  Designation VARCHAR(20) NOT NULL,
  Salary INT NOT NULL DEFAULT(25000),
  
  CONSTRAINT joining_yr CHECK(JoiningYear >= 2000),
  CONSTRAINT birthday CHECK(Birthday <= '2000-12-31')
);

INSERT INTO employee(EmpName, JoiningYear, Birthday, Designation) VALUE("Arnab", 2020, "1990-12-1", "SWE");