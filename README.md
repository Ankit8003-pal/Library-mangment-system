📘 Project Information

Name: Ankit Kumar
Roll No: 2501940052
University Name: K.R. Mangalam University
Date: 25-11-2025
Assignment: 03 – Python Object-Oriented Library Inventory System

📄 Summary

This project implements a Library Inventory System using Python and Object-Oriented Programming (OOP).
The system models real-world items like Book and Member to manage library operations such as adding books, registering users, borrowing books, returning books, and storing all data for later use.

This assignment belongs to the course Programming for Problem Solving Using Python
(Course Code: ETCCPP171) for the MCA (AI & ML) program, Semester I.

The objective of this project is to apply:

Basic and advanced OOP concepts

Modular program design

File handling (JSON + CSV)

Error handling

Real-world system modeling

🧩 Main Points and Implementation Details
🎯 Objective

To design and implement Python classes, use attributes and methods, apply modular programming, and store data permanently using files.

📁 Modular Structure

The project is arranged inside a folder named library_system, which contains the following files:

1. book.py

Defines the Book class with attributes:

title, author, isbn, and available
And methods:

borrow()

return_book()

2. member.py

Defines the Member class with attributes:

name, member_id, and borrowed_books
And methods:

borrow_book()

return_book()

list_books()

3. library.py

Contains the Library class, which manages the complete system.
The core functions include:
a. add_book() – Add new books
b. register_member() – Register new members
c. lend_book() – Issue a book
d. take_return() – Accept returned books

💾 File Persistence (Task 4)

The system stores and loads all data using JSON and CSV files.
This ensures that books and member data remain saved even after closing the program.

Includes:

Error handling for missing or corrupted files

Safe loading and saving of data

📊 Analytics (Task 5)

The system includes a simple report feature, such as:

Total active members

Total borrowed books

Available books

Other class-level analytics if needed

🖥️ Interactive Console Menu (Bonus Task 6)

The main.py file contains a clear and easy-to-use menu that allows users to:

Add a new book

Register a new member

Borrow a book

Return a book

View the library report

Save data (JSON + CSV)

Load data (JSON + CSV)

View all books

View all members

Exit the program

This makes the program user-friendly and easy to operate.
