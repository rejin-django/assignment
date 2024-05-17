# Employee Management System

## Overview
The Employee Management System is a command-line application developed in Python. It allows companies to manage employee and department information using Object-Oriented Programming (OOP) principles and efficient data structures.

## Features
- Add and remove departments.
- Add and remove employees.
- Display all departments.
- List all employees in a specific department.
- Save company data to a file.
- Load company data from a file.

## Project Structure
The project is divided into multiple Python scripts for better organization and modularity:
- `employee.py`: Contains the `Employee` class with attributes and methods related to employees.
- `department.py`: Contains the `Department` class with attributes and methods related to departments.
- `company.py`: Contains the `Company` class for managing the overall company structure and employee-department interactions.
- `main.py`: The main script that provides the command-line interface for user interaction.
- `test_employee_management.py`: Contains unit tests for validating the functionality of the classes and methods.

## Installation and Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/employee-management-system.git
    cd employee-management-system
    ```

2. Ensure you have Python installed (version 3.6 or higher recommended).

3. Run the main script to start the application:
    ```sh
    python main.py
    ```

## Usage
1. Run the `main.py` script:
    ```sh
    python main.py
    ```

2. Follow the on-screen menu to interact with the system:
    - Add Department
    - Remove Department
    - Add Employee
    - Remove Employee
    - Display Departments
    - List Employees in Department
    - Save Data
    - Load Data
    - Exit

3. Input the required information as prompted by the menu options.

## Data Persistence
- The system allows you to save the current state of the company data to a file.
- You can also load data from a file when starting the system to restore previous states.

## Unit Tests
- The `test_employee_management.py` script contains unit tests to ensure the correctness of the system.
- To run the tests, use the following command:
    ```sh
    python -m unittest test_employee_management.py
    ```

## Comments and Design Decisions
- **Encapsulation**: Employee and Department attributes are managed through class methods.
- **Error Handling**: The system checks for the existence of departments and employees to avoid errors.
- **Data Persistence**: Saving and loading of company data are handled using JSON for simplicity.
- **Unit Tests**: Basic tests validate the functionality of core methods.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss potential changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Thanks to everyone who provided feedback and suggestions for improving this project.


