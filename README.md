# JustInvestSystem

This project is a simulation of a secure login system for a fictional investment platform called `JustInvestSystem`. It includes robust testing using Python's `unittest` framework to ensure functionality and reliability.**Object-Oriented Design (OOD)** and **SOLID principles**, ensuring that the system is modular, extensible, and easy to maintain.

---

## Features

- **Secure Login System**: Hashes passwords with salts for enhanced security.
- **Role-Based Access**: Identifies users' roles after successful login.
- **File-Based User Records**: Reads and verifies user credentials from a password file.

---

## How to Run the Code

### Running the Main Application

1. **Navigate to the Root Directory**:
   Ensure you are in the root directory where the `main.py` file is located.

2. **Run the Application**:
   - For Linux/macOS:
     ```bash
     python3 main.py
     ```
   - For Windows:
     ```bash
     python main.py
     ```

---

### Running Tests

1. **Run Individual Test Files**:
   Use the following commands to run specific test files:

   - For Linux/macOS:
     ```bash
     python3 problem4.py
     python3 problem3.py
     # Add similar commands for other test files
     ```
   - For Windows:
     ```bash
     python problem4.py
     python problem3.py
     # Add similar commands for other test files
     ```


**Object-Oriented Design Patterns**
   - **Encapsulation**: Classes like `rbac`, `JustInvestSystem`, and `PasswordFile` encapsulate their functionalities, keeping related data and methods together.
   - **Inheritance**: The user roles such as `Client`, `Employee`, and `FinancialPlanner` inherit from the base class `User`, promoting code reuse.
   - **Polymorphism**: The `get_permissions()` method in user role classes demonstrates polymorphism, allowing behavior to be overridden by derived classes.