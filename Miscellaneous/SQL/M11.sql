CREATE DATABASE StudentLibManagementSytem;
USE StudentLibManagementSytem;

CREATE TABLE Student(
	roll VARCHAR(4) PRIMARY KEY,
    name VARCHAR(30)
);

CREATE TABLE Book(
	book_id VARCHAR(4) PRIMARY KEY,
    name VARCHAR(30),
    genre VARCHAR(10)
);

CREATE TABLE Borrow(
	student_roll VARCHAR(4),
    book_id VARCHAR(4),
    b_date DATE,
    return_date DATE,
    
    FOREIGN KEY (student_roll) REFERENCES Student(roll),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    
    PRIMARY KEY(student_roll, book_id)
);

CREATE TABLE Librarian(
	lib_id VARCHAR(4) PRIMARY KEY,
    name VARCHAR(30)
);


CREATE TABLE Permission(
	book_id VARCHAR(4),
    lib_id VARCHAR(4),
    
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (lib_id) REFERENCES Librarian(lib_id)
);