# test.py

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        # Reset the employee count before each test case
        Employee.employee_count = 0

    def test_employee_creation(self):
        """Test that an employee is created with correct attributes and count is incremented."""
        emp = Employee("John Doe", "HR", 50000)
        self.assertEqual(emp.name, "John Doe")
        self.assertEqual(emp.department, "HR")
        self.assertEqual(emp.salary, 50000)
        self.assertEqual(Employee.employee_count, 1)

    def test_display_employee(self):
        """Test that the display_employee method returns a correctly formatted string."""
        emp = Employee("Jane Doe", "IT", 60000)
        display_str = emp.display_employee()
        self.assertIn("Jane Doe", display_str)
        self.assertIn("IT", display_str)
        self.assertIn("60000.00", display_str)

    def test_apply_raise(self):
        """Test that applying a 10% raise updates the salary correctly."""
        emp = Employee("Jim Beam", "Sales", 70000)
        emp.apply_raise(10)  # Applying a 10% raise should update salary to 77000
        self.assertAlmostEqual(emp.salary, 77000, places=2)

    def test_apply_raise_zero(self):
        """Test that applying a 0% raise leaves the salary unchanged."""
        emp = Employee("Alice", "Marketing", 80000)
        emp.apply_raise(0)
        self.assertAlmostEqual(emp.salary, 80000, places=2)

    def test_apply_raise_negative(self):
        """Test that applying a negative raise (a salary cut) updates the salary correctly."""
        emp = Employee("Bob", "Finance", 100000)
        emp.apply_raise(-10)  # Applying a -10% 'raise' should reduce the salary to 90,000
        self.assertAlmostEqual(emp.salary, 90000, places=2)

    def test_multiple_employees_count(self):
        """Test that creating multiple employees correctly increments the employee count."""
        employees = [Employee(f"Emp{i}", "Dept", 50000 + i * 1000) for i in range(5)]
        self.assertEqual(Employee.employee_count, 5)

    def test_multiple_raise_calls(self):
        """Test that applying multiple raises sequentially produces the correct cumulative salary."""
        emp = Employee("Charlie", "Research", 50000)
        emp.apply_raise(10)  # First raise: 50000 * 1.10 = 55000
        emp.apply_raise(20)  # Second raise: 55000 * 1.20 = 66000
        self.assertAlmostEqual(emp.salary, 66000, places=2)

if __name__ == "__main__":
    unittest.main()
