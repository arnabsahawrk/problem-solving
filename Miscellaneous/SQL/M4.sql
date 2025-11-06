CREATE DATABASE m4assignment;
USE m4assignment;

CREATE TABLE student
(
  student_id INT AUTO_INCREMENT  PRIMARY KEY,
  roll_no VARCHAR(20) UNIQUE NOT NULL,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50),
  gender ENUM("Male", "Female", "Other"),
  date_of_birth DATE CHECK(date_of_birth <='2000-12-31'),
  registration_year INT CHECK(registration_year >= 2000),
  course VARCHAR(50),
  department VARCHAR(50),
  year_of_study INT CHECK(year_of_study BETWEEN 1 AND 5),
  email VARCHAR(100) UNIQUE,
  phone VARCHAR(15),
  address TEXT,
  status ENUM('Active', 'Dropped', 'Alumni') DEFAULT 'Active'
);

CREATE TABLE library
(
  issue_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT,
  roll_no VARCHAR(20),
  book_id INT NOT NULL,
  issue_date DATE,
  return_date DATE,
  
  UNIQUE(student_id, roll_no),
  FOREIGN KEY (student_id) REFERENCES student(student_id),
  FOREIGN KEY (roll_no) REFERENCES student(roll_no)
);

CREATE TABLE fees
(
  fee_id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT UNIQUE,
  roll_no VARCHAR(20) UNIQUE,
  amount DECIMAL(10, 2),
  status ENUM('Pending', 'Paid', 'Cancelled') DEFAULT 'Pending',
  
  FOREIGN KEY (student_id) REFERENCES student(student_id),
  FOREIGN KEY (roll_no) REFERENCES student(roll_no)
);

INSERT INTO student 
(roll_no, first_name, last_name, gender, date_of_birth, registration_year, course, department, year_of_study, email, phone, address, status)
VALUES
('CSE2024-001', 'Arnab', 'Saha', 'Male', '2000-05-14', 2024, 'BSc Computer Science', 'CSE', 1, 'arnab@univ.edu', '01710000001', 'Dhaka', 'Active'),
('CSE2023-002', 'Priya', 'Das', 'Female', '1999-03-22', 2023, 'BSc Computer Science', 'CSE', 2, 'priya@univ.edu', '01710000002', 'Chittagong', 'Active'),
('EEE2022-003', 'Hasib', 'Ahmed', 'Male', '1998-09-18', 2022, 'BSc Electrical', 'EEE', 3, 'hasib@univ.edu', '01710000003', 'Khulna', 'Active'),
('BBA2021-004', 'Rafi', 'Hossain', 'Male', '1999-11-10', 2021, 'BBA', 'Business', 4, 'rafi@univ.edu', '01710000004', 'Rajshahi', 'Active'),
('CSE2024-005', 'Sumaiya', 'Khan', 'Female', '2000-01-20', 2024, 'BSc Computer Science', 'CSE', 1, 'sumaiya@univ.edu', '01710000005', 'Sylhet', 'Active'),
('EEE2023-006', 'Tariq', 'Mahmud', 'Male', '1997-04-05', 2023, 'BSc Electrical', 'EEE', 2, 'tariq@univ.edu', '01710000006', 'Barisal', 'Dropped'),
('BBA2022-007', 'Nusrat', 'Akter', 'Female', '1999-07-25', 2022, 'BBA', 'Business', 3, 'nusrat@univ.edu', '01710000007', 'Comilla', 'Active'),
('CSE2021-008', 'Jamil', 'Uddin', 'Male', '1998-12-10', 2021, 'BSc Computer Science', 'CSE', 4, 'jamil@univ.edu', '01710000008', 'Mymensingh', 'Alumni'),
('EEE2024-009', 'Afsana', 'Rahman', 'Female', '2000-03-03', 2024, 'BSc Electrical', 'EEE', 1, 'afsana@univ.edu', '01710000009', 'Rangpur', 'Active'),
('BBA2023-010', 'Tanvir', 'Islam', 'Male', '1999-08-19', 2023, 'BBA', 'Business', 2, 'tanvir@univ.edu', '01710000010', 'Gazipur', 'Active');

INSERT INTO library (student_id, roll_no, book_id, issue_date, return_date)
VALUES
(1, 'CSE2024-001', 101, '2024-05-01', '2024-05-10'),
(2, 'CSE2023-002', 102, '2024-04-15', '2024-04-25'),
(3, 'EEE2022-003', 103, '2024-03-10', '2024-03-20'),
(4, 'BBA2021-004', 104, '2024-02-05', '2024-02-20'),
(5, 'CSE2024-005', 105, '2024-06-01', '2024-06-10'),
(6, 'EEE2023-006', 106, '2024-07-12', '2024-07-25'),
(7, 'BBA2022-007', 107, '2024-05-30', '2024-06-05'),
(8, 'CSE2021-008', 108, '2024-01-10', '2024-01-20'),
(9, 'EEE2024-009', 109, '2024-06-15', '2024-06-25'),
(10, 'BBA2023-010', 110, '2024-03-01', '2024-03-15');


INSERT INTO fees (student_id, roll_no, amount, status)
VALUES
(1, 'CSE2024-001', 50000.00, 'Paid'),
(2, 'CSE2023-002', 48000.00, 'Paid'),
(3, 'EEE2022-003', 47000.00, 'Pending'),
(4, 'BBA2021-004', 45000.00, 'Paid'),
(5, 'CSE2024-005', 50000.00, 'Pending'),
(6, 'EEE2023-006', 48000.00, 'Cancelled'),
(7, 'BBA2022-007', 46000.00, 'Paid'),
(8, 'CSE2021-008', 44000.00, 'Paid'),
(9, 'EEE2024-009', 49000.00, 'Pending'),
(10, 'BBA2023-010', 47000.00, 'Pending');

SELECT * FROM student;
SELECT * FROM library;
SELECT * FROM fees;

SET SQL_SAFE_UPDATES = 0;
UPDATE student SET status = 'Dropped' WHERE student_id = 5;
DELETE FROM student WHERE student_id = 10;
SET SQL_SAFE_UPDATES = 1;

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Age INT,
    Department VARCHAR(50)
);

INSERT INTO Employee (EmployeeID, FirstName, LastName, Age, Department) VALUES
(1, 'John', 'Doe', 28, 'Sales'),
(2, 'Jane', 'Smith', 32, 'Marketing'),
(3, 'Michael', 'Johnson', 35, 'Finance'),
(4, 'Sarah', 'Brown', 30, 'HR'),
(5, 'William', 'Davis', 25, 'Engineering'),
(6, 'Emily', 'Wilson', 28, 'Sales'),
(7, 'Robert', 'Lee', 33, 'Marketing'),
(8, 'Laura', 'Hall', 29, 'Finance'),
(9, 'Thomas', 'White', 31, 'HR'),
(10, 'Olivia', 'Clark', 27, 'Engineering');

SELECT DISTINCT Department FROM Employee;

SELECT LastName FROM Employee ORDER BY Age DESC;

SELECT LastName FROM Employee WHERE Age > 30 AND Department = "Marketing";

SELECT * FROM Employee;

SELECT * FROM Employee WHERE FirstName LIKE '%son%' OR LastName Like '%son%';

SELECT * FROM Employee WHERE Department = 'Engineering';
