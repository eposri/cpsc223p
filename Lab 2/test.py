import unittest
from assignment1 import (  # Replace `your_file_name` with the actual file name (without .py).
    multiply_and_divide,
    modulus,
    power_operations,
    split_name,
    case_conversion,
    reverse_string,
    create_food_list,
    add_food_items,
    remove_food_item,
    sort_food_list
)

class TestFunctions(unittest.TestCase):
    # Numbers Section
    def test_multiply_and_divide(self):
        self.assertEqual(multiply_and_divide(6, 3, 2), 9.0)
        self.assertEqual(multiply_and_divide(10, 5, 2), 25.0)
        self.assertRaises(ZeroDivisionError, multiply_and_divide, 6, 3, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(20, 4), 0)

    def test_power_operations(self):
        result = power_operations(4)
        self.assertEqual(result["square"], 16)
        self.assertEqual(result["cube"], 64)
        self.assertEqual(result["pow_square"], 16)
        self.assertEqual(result["pow_cube"], 64)

    # Strings Section
    def test_split_name(self):
        self.assertEqual(split_name("John Doe"), {"first_name": "John", "last_name": "Doe"})
        self.assertEqual(split_name("Alice"), {"first_name": "Alice", "last_name": ""})

    def test_case_conversion(self):
        self.assertEqual(case_conversion("John Doe"), {"uppercase": "JOHN DOE", "lowercase": "john doe"})

    def test_reverse_string(self):
        self.assertEqual(reverse_string("John Doe"), "eoD nhoJ")
        self.assertEqual(reverse_string("abcd"), "dcba")

    # Lists Section
    def test_create_food_list(self):
        food_list = create_food_list()
        self.assertIsInstance(food_list, list)
        self.assertGreaterEqual(len(food_list), 5)

    def test_add_food_items(self):
        initial_list = ["pizza", "pasta"]
        updated_list = add_food_items(initial_list, ["sushi", "burger"])
        self.assertIn("sushi", updated_list)
        self.assertIn("burger", updated_list)

    def test_remove_food_item(self):
        food_list = ["pizza", "pasta", "sushi"]
        updated_list = remove_food_item(food_list, "pizza")
        self.assertNotIn("pizza", updated_list)

    def test_sort_food_list(self):
        unsorted_list = ["pizza", "sushi", "burger"]
        sorted_list = sort_food_list(unsorted_list)
        self.assertEqual(sorted_list, ["burger", "pizza", "sushi"])


if __name__ == "__main__":
    unittest.main()
