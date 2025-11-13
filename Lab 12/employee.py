'''
Name: Kayla Ngo
CWID: 885083436
Date: 11/12/2025
'''

class Employee:
    employee_count = 0 # Class variable
    def __init__(self, name, department, salary):
        '''
        initializer
        three parameters (attributes): name, dept, salary
        '''
        #self.name = str(name) auto string, don't need type conversion
        #self.department = str(department)
        self.name = name
        self.department = department
        self.salary = float(salary)
        Employee.employee_count += 1 # incrementor


    # employee_count = 0 goes before constructor

    def display_employee(self) -> str:
        '''
        displays employee's name, dept, current salary
        return: formatted string
        '''
        return f"Name: {self.name}, Department: {self.department}, Salary: {self.salary:.2f}"
    
    def apply_raise(self, raise_percentage: float):
        '''s
        apply a raise to the employee's salary
        input: a float representing the raise percentage (ex. 10 for 10% raise)
        '''
        self.salary *= (1 + raise_percentage / 100)

    def change_dept(self, new_dept):
        self.department = new_dept
