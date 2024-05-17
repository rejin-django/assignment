import unittest
from employee import Employee
from department import Department
from company import Company

class TestEmployeeManagement(unittest.TestCase):
    
    def test_employee_creation(self):
        emp = Employee("John Doe", "001", "Developer", "IT")
        self.assertEqual(emp.name, "John Doe")
        self.assertEqual(emp.emp_id, "001")
        self.assertEqual(emp.title, "Developer")
        self.assertEqual(emp.department, "IT")
    
    def test_department_operations(self):
        dept = Department("IT")
        emp = Employee("John Doe", "001", "Developer", "IT")
        dept.add_employee(emp)
        self.assertIn(emp, dept.employees)
        self.assertTrue(dept.remove_employee("001"))
        self.assertFalse(dept.remove_employee("002"))

    def test_company_operations(self):
        company = Company()
        company.add_department("IT")
        self.assertIn("IT", company.display_departments())
        company.add_employee_to_department("John Doe", "001", "Developer", "IT")
        self.assertEqual(len(company.list_employees_in_department("IT")), 1)
        company.remove_employee_from_department("001", "IT")
        self.assertEqual(len(company.list_employees_in_department("IT")), 0)
        company.remove_department("IT")
        self.assertNotIn("IT", company.display_departments())

if __name__ == "__main__":
    unittest.main()
