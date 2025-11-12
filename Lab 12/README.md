# Laboratory: Python Classes and Object-Oriented Programming

## Laboratory Objectives

   1. Understand and apply the core principles of object-oriented programming (OOP) using Python classes.
   2. Learn how to create and instantiate classes as well as differentiate between instance and class variables.
   3. Develop methods for manipulating object state and observe how attributes and method objects behave.
   4. Gain experience in structuring a Python project with multiple modules, a main driver program, and automated tests.

## Getting Started

1. Setting Up Python Environment

     - Verify Python Installation:
     - Open your terminal (Command Prompt for Windows, Terminal for macOS/Linux).
     - Type python --version and press Enter.
     - You should see the installed Python version displayed.

2. Configuring Visual Studio Code (VS Code)

     - Install Python Extension:
     - Open VS Code.
     - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
     - Search for “Python” in the Extensions Marketplace.
     - Click “Install” on the Python extension by Microsoft.

3. Running Python in VS Code

     - Create a New Python File:
     - In VS Code, open a folder where you want to save your Python projects.
     - Click on File > New File or press Ctrl+N to create a new file.
     - Save the file with a .py extension (e.g., hello.py).
     
## Program Instructions

## Part 1: Create the Employee Module
1. File: `employee.py`
2. Requirements:
     * Define a Class Named Employee: 
          * Initialization Method (__init__):
               - Accept three parameters: name (string), department (string), and salary (float).
               - Set instance variables for each parameter (e.g., self.name, self.department, and self.salary).
               - Maintain a class variable named employee_count to track the total number of employees. This variable should be incremented every time a new instance is created.

     * Methods:
          * display_employee Method:
               - Return a formatted string that displays the employee's name, department, and current salary.
          * apply_raise Method:
               - Accept a single parameter representing the raise percentage (for example, 10 for a 10% increase).
               - Adjust the employee’s salary accordingly.
          * (30 points) Additional Methods:
               - You may include extra methods (such as updating the department) to further demonstrate your understanding of instance and class behaviors.

## Part 2: Create the Main Driver Program
1. Create a `main.py` driver program to meet the following requirements:
2. Functionality:
     - Import the Employee class from the employee.py module.
     - Implement a text-based menu that repeats until the user chooses to exit. The menu should display the following options:

*** EMPLOYEE MANAGEMENT SYSTEM ***

1. Add Employee
2. Display All Employees
3. Apply Raise to an Employee
9. Exit

     - Menu Options:
          1. Add Employee:
               - Prompt the user for the employee’s name, department, and salary.
               - Create an instance of Employee using these inputs and store the instance in a list.
          2. Display All Employees:
               - Iterate over the list of employee instances.
               - Use each employee’s display_employee method to print a neatly formatted summary.
               - Also display the total number of employees by referencing the class variable employee_count.
          3. Apply Raise to an Employee:
               - Prompt the user to enter the employee’s name and the raise percentage.
               - If an employee matching the name exists in your list, invoke the apply_raise method to update their salary.
               - If no match is found, display a message indicating that the employee does not exist.
          4. Exit:
               - Terminate the program.


* Run the program using the command below and repeat the steps above until you are satisfied your program output meets the above requirements.

    ```
    python3 main.py
    ```


* Typical input and output for the program:
    
    *** EMPLOYEE MANAGEMENT SYSTEM ***
1. Add Employee
2. Display All Employees
3. Apply Raise to an Employee
4. Exit
<br/>

Enter menu choice: 1

Enter employee name: Alice Smith

Enter department: Sales

Enter salary: 55000

*** EMPLOYEE MANAGEMENT SYSTEM ***
1. Add Employee
2. Display All Employees
3. Apply Raise to an Employee
4. Exit

Enter menu choice: 1

Enter employee name: Bob Johnson

Enter department: IT

Enter salary: 70000

*** EMPLOYEE MANAGEMENT SYSTEM ***
1. Add Employee
2. Display All Employees
3. Apply Raise to an Employee
4. Exit

Enter menu choice: 3

Enter employee name: Alice Smith

Enter raise percentage: 10

*** EMPLOYEE MANAGEMENT SYSTEM ***
1. Add Employee
2. Display All Employees
3. Apply Raise to an Employee
4. Exit

Enter menu choice: 2

Employee Details:

Name: Alice Smith, Department: Sales, Salary: 60500.00

Name: Bob Johnson, Department: IT, Salary: 70000.00

Total Employees: 2

*** EMPLOYEE MANAGEMENT SYSTEM ***
1. Add Employee
2. Display All Employees
3. Apply Raise to an Employee
4. Exit

Enter menu choice: 4


1. Run the unit testing program to ensure that your program runs as expected.

    ```
    ./test.sh
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` repeatedly until it passes all the test.

## Submission

Submit a zip file containing all the code files on canvas 

Naming Convention: <CWID>_<LastName>.zip  

You should have the following files:
```
main.py
employee.py
test.py
test.sh
win_test.bat
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below.  Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|5|main.py file submitted contains the main driver program and meets the program requirements|
|5|employee.py file submitted contains the flights module and meets the program requirements|
|10|unit testing|
|30|extra methods|
