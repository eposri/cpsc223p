'''
Name: Kayla Ngo
CWID: 885083436
Date: 11/12/2025
'''
from employee import Employee

def print_menu():
    print("\n*** EMPLOYEE MANAGEMENT SYSTEM ***")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Apply Raise to an Employee")
    print("4. ")
    print("5. Change an Employee's Department")
    print("6. Terminate an Employee")
    print("7. Exit")

def main():
    employees = []
    
    while True:
        print_menu()
        choice = input("Enter menu choice: ").strip()

        if choice == "1":
            name = input("Enter employee name: ").strip()
            department = input("Enter department: ").strip()
            salary_input = input("Enter salary: ").strip()
            try:
                salary = float(salary_input)
            except ValueError:
                print("Invalid salary input. Salary must be a number.")
                continue
            e = Employee(name, department, salary)
            employees.append(e)
        elif choice == "2":
            if not employees:
                print("No employees to display.")
            else:
                print("\nEmployee Details:")
                for e in employees:
                    print(e.display_employee())
                print(f"Total Employees: {Employee.employee_count}")
        elif choice == "3":
            # checking if employee list is empty 
            if not employees:
                print("No employees available to apply a raise to.")
            else:
                name_to_update = input("Enter employee name: ").strip()
                for e in employees:
                    if e.name == name_to_update:
                        raise_percentage_input = input("Enter raise percentage: ").strip()
                        try:
                            raise_percentage = float(raise_percentage_input)
                        except ValueError:
                            print("Invalid raise percentage. Must be a number.")
                            break
                        e.apply_raise(raise_percentage_input)
                        print(f"Applied {raise_percentage}% raise to {e.name}. New salary is {e.salary:.2f}.")
                        break
                else: # inputted employee DNE in our list
                    print("Employee does not exist.")
        elif choice == "4":

        elif choice == "5":
            # change employee's dept
            if not employees:
                print("No employees available to change departments.")
            else:
                name_to_update = input("Enter employee name: ").strip()
                for e in employees:
                    if e.name == name_to_update:
                        dept_to_update = input("Enter name of new department:" ).strip()
                        
                        e.apply_raise(raise_percentage_input)
                        print(f"Applied {raise_percentage}% raise to {e.name}. New salary is {e.salary:.2f}.")
                        break
                else: # inputted employee DNE in our list
                    print("Employee does not exist.")
        elif choice == "6":
            # terminate employee

        elif choice == "7":
            print("Exiting program. . .")
            break
        else:
            print("Invalid menu choice. Please try again.")

if __name__ == "__main__":
    main()