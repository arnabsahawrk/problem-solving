CREATE DATABASE finalExam;
USE finalExam;

CREATE TABLE Instructor (	
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,	
    Name VARCHAR(255) NOT NULL,	
    Email VARCHAR(255) NOT NULL UNIQUE,	
    Phone VARCHAR(15),	
    Department VARCHAR(50)	
);	

CREATE TABLE Course (	
    CourseID INT AUTO_INCREMENT PRIMARY KEY,	
    Title VARCHAR(255) NOT NULL,	
    Credits INT NOT NULL,	
    InstructorID INT,	
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)	
);	

CREATE TABLE Student (	
    StudentID INT AUTO_INCREMENT PRIMARY KEY,	
    Name VARCHAR(255) NOT NULL,	
    Email VARCHAR(255) NOT NULL UNIQUE,	
    Phone VARCHAR(15)	
);

CREATE TABLE Enrollment (	
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,	
    StudentID INT,	
    CourseID INT,	
    EnrollmentDate DATE NOT NULL,	
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),	
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID)	
);	

INSERT INTO Instructor (Name, Email, Phone, Department) VALUES
('Dr. Sarah Ahmed', 'sarah.ahmed@uni.edu', '01711111111', 'Computer Science'),
('Prof. Karim Hassan', 'karim.hassan@uni.edu', '01722222222', 'Mathematics'),
('Dr. Fatima Rahman', 'fatima.rahman@uni.edu', '01733333333', 'Computer Science'),
('Prof. Rahim Khan', 'rahim.khan@uni.edu', '01744444444', 'Physics'),
('Dr. Nazia Islam', 'nazia.islam@uni.edu', '01755555555', 'Mathematics');

INSERT INTO Instructor (InstructorID, Name, Email, Phone, Department)
VALUES (10, 'Dr. New Instructor', 'new.instructor@uni.edu', '01799999999', 'Computer Science');

INSERT INTO Student (Name, Email, Phone) VALUES
('Ashraf Ali', 'ashraf@student.edu', '01611111111'),
('Mehreen Sultana', 'mehreen@student.edu', '01622222222'),
('Tanvir Hossain', 'tanvir@student.edu', '01633333333'),
('Sabrina Khan', 'sabrina@student.edu', '01644444444'),
('Farhan Ahmed', 'farhan@student.edu', '01655555555'),
('Ayesha Siddique', 'ayesha@student.edu', '01666666666'),
('Rahat Mahmud', 'rahat@student.edu', '01677777777');

INSERT INTO Course (Title, Credits, InstructorID) VALUES
('Database Systems', 3, 1),
('Data Structures', 3, 1),
('Linear Algebra', 4, 2),
('Calculus I', 4, 2),
('Web Development', 3, 3),
('Machine Learning', 4, 3),
('Quantum Physics', 5, 4),
('Discrete Mathematics', 3, 5);

INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate) VALUES
(1, 1, '2024-09-01'),
(1, 2, '2024-09-01'),
(1, 5, '2024-09-02'),
(1, 6, '2024-09-02'),
(2, 3, '2024-09-01'),
(2, 4, '2024-09-01'),
(2, 8, '2024-09-03'),
(3, 1, '2024-09-02'),
(3, 7, '2024-09-02'),
(4, 2, '2024-09-01'),
(4, 5, '2024-09-01'),
(4, 6, '2024-09-02'),
(5, 3, '2024-09-03'),
(6, 1, '2024-09-01'),
(6, 4, '2024-09-01'),
(7, 6, '2024-09-02'),
(7, 7, '2024-09-02'),
(7, 8, '2024-09-03');

INSERT INTO Enrollment (StudentID, CourseID, EnrollmentDate)
VALUES (
 5,
 (SELECT CourseID FROM Course ORDER BY Credits DESC LIMIT 1),
 CURDATE()
);

SET SQL_SAFE_UPDATES = 0;
UPDATE Course
SET InstructorID = 10
WHERE CourseID = 3;
SET SQL_SAFE_UPDATES = 1;

SELECT I.Name, SUM(C.Credits) AS TotalCredits
FROM Instructor I
JOIN Course C ON I.InstructorID = C.InstructorID
GROUP BY I.InstructorID, I.Name
ORDER BY TotalCredits DESC
LIMIT 1;

SELECT S.StudentID, S.Name, COUNT(E.CourseID) AS CourseCount
FROM Student S
JOIN Enrollment E ON S.StudentID = E.StudentID
GROUP BY S.StudentID, S.Name
HAVING COUNT(E.CourseID) > 2;

SELECT InstructorID, SUM(Credits) AS TotalCredits
FROM Course
GROUP BY InstructorID;

SELECT Title, Credits
FROM Course
ORDER BY Credits DESC;

SELECT MAX(Salary) AS SecondHighestSalary
FROM Instructor
WHERE Salary < (SELECT MAX(Salary) FROM Instructor);

CREATE TABLE Course (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Credits INT NOT NULL,
    InstructorID INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
    ON DELETE CASCADE
);

