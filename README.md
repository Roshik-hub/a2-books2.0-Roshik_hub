# Assignment 2 - Reading Tracker

## Project Overview

The Reading Tracker App is a Python program built using Kivy that allows users to manage a personal list of books they want to read. Users can:

Add new books (title, author, number of pages)

Mark books as completed or unread

Sort books by title, author, or number of pages

View the total number of pages still to read

Save changes to a JSON file so data persists between sessions

The app demonstrates object-oriented programming (OOP) concepts, error handling, and GUI programming in Python.
## Reflection

### 1. What did you learn about coding from this assignment?
Importance of writing clean and structured code.

Using classes and methods reduces duplication and simplifies data management.

Implementing robust error handling prevents crashes with invalid input.

Learned how to persist data using JSON files.

Linking backend logic with GUI taught me event-driven programming.

Meaningful variable names, constants, and comments improve readability and maintainability.

### 2. What did you learn about program design?
Following the Single Responsibility Principle (SRP) keeps code organized.

Book handles book data; BookCollection manages collections; main.py handles GUI.

Separating GUI into a .kv file separates interface from logic.

Modular design makes testing and maintenance easier.

Dynamic widget creation in Kivy can connect UI elements to backend objects effectively.

### 3. How did you use version control?
Made incremental commits for each step of development.

Committed Book and BookCollection classes first.

Tested console program thoroughly before committing.

### 4. What would you improve next time?
Spend more time planning program structure before coding.

Write detailed tests for edge cases early.

Refactor GUI code sooner to improve dynamic updates.
