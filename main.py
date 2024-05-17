from company import Company

def print_menu():
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Add Employee")
    print("4. Remove Employee")
    print("5. Display Departments")
    print("6. List Employees in Department")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")

def main():
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            dept_name = input("Enter department name: ")
            company.add_department(dept_name)
        elif choice == '2':
            dept_name = input("Enter department name: ")
            company.remove_department(dept_name)
        elif choice == '3':
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            dept_name = input("Enter department name: ")
            company.add_employee_to_department(name, emp_id, title, dept_name)
        elif choice == '4':
            emp_id = input("Enter employee ID: ")
            dept_name = input("Enter department name: ")
            company.remove_employee_from_department(emp_id, dept_name)
        elif choice == '5':
            print("Departments: ", company.display_departments())
        elif choice == '6':
            dept_name = input("Enter department name: ")
            print("Employees: ", company.list_employees_in_department(dept_name))
        elif choice == '7':
            filename = input("Enter filename to save data: ")
            company.save_data(filename)
        elif choice == '8':
            filename = input("Enter filename to load data: ")
            company.load_data(filename)
        elif choice == '9':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
