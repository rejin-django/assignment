from employee import Employee
from department import Department
import json

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, dept_name):
        if dept_name not in self.departments:
            self.departments[dept_name] = Department(dept_name)
        else:
            print("Department already exists.")

    def remove_department(self, dept_name):
        if dept_name in self.departments:
            del self.departments[dept_name]
        else:
            print("Department does not exist.")

    def add_employee_to_department(self, name, emp_id, title, dept_name):
        if dept_name in self.departments:
            new_employee = Employee(name, emp_id, title, dept_name)
            self.departments[dept_name].add_employee(new_employee)
        else:
            print("Department does not exist.")

    def remove_employee_from_department(self, emp_id, dept_name):
        if dept_name in self.departments:
            if not self.departments[dept_name].remove_employee(emp_id):
                print("Employee not found in department.")
        else:
            print("Department does not exist.")

    def display_departments(self):
        return list(self.departments.keys())

    def list_employees_in_department(self, dept_name):
        if dept_name in self.departments:
            return self.departments[dept_name].list_employees()
        else:
            print("Department does not exist.")
            return []

    def save_data(self, filename):
        data = {dept: [emp.__dict__ for emp in self.departments[dept].employees] for dept in self.departments}
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for dept, employees in data.items():
                    self.add_department(dept)
                    for emp_data in employees:
                        self.add_employee_to_department(emp_data['name'], emp_data['emp_id'], emp_data['title'], dept)
        except FileNotFoundError:
            print("No saved data found.")
