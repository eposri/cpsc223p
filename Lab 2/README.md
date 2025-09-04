# Assignment 1

## Laboratory Objectives
1. Write Python code to implement basic operations with numbers, strings, and lists.
2. Execute the program from the command line.
3. Unit test the program using a testing script.
4. Upload the assignment on Canvas for submission.

---

## Program Instructions

1. **Create a `assignment1.py` module to meet the following requirements**:

   1. **Create a file named `assignment1.py`.**

   2. **Add below comments at the top of your code:**<br/>
      Name: Your Name<br/>
      Date: 09/03/2025<br/>
      File Purpose: Demonstrates numbers, strings, and list operations
     
   3. **Implement a "numbers" section with these functions:**

      - Define a function named `multiply_and_divide(a, b, c)`:
        - Multiplies `a` and `b`, then divides the result by `c`.
        - Returns the final result.

      - Define a function named `modulus(a, b)`:
        - Returns the remainder when `a` is divided by `b`.

      - Define a function named `power_operations(num)`:
        - Calculates and returns the square and cube of `num` using both `**` and `pow()`. 
        - Note: The function should return a dict that has specific keys: "square", "cube", "pow_square", "pow_cube".

   4. **Implement a "strings" section with these functions:**

      - Define a function named `print_name(name)`:
        - Prints the full name (just outputs the string).

      - Define a function named `split_name(name)`:
        - Splits `name` into two parts: first name and last name.
        - Returns both names in a dictionary with keys `"first_name"` and `"last_name"`.

      - Define a function named `case_conversion(name)`:
        - Converts `name` to uppercase and lowercase.
        - Returns both versions in a dictionary.

      - Define a function named `reverse_string(name)`:
        - Reverses the order of characters in `name`.
        - Returns the reversed string.

   5. **Implement a "lists" section with these functions:**

      - Define a function named `create_food_list()`:
        - Returns a list of at least five of your favorite foods.

      - Define a function named `add_food_items(food_list, items)`:
        - Accepts an existing `food_list` and a list of new `items`.
        - Adds (extends) the new items to the existing list.
        - Returns the updated list.

      - Define a function named `remove_food_item(food_list, item)`:
        - Removes an `item` from the `food_list`.
        - Returns the updated list.

      - Define a function named `sort_food_list(food_list)`:
        - Sorts the `food_list` alphabetically.
        - Returns the sorted list.

2. **At the bottom of the `assignment1.py` file**, paste the "driver" section (mentioned below) to test each function manually:
   ```python
   if __name__ == "__main__":
       # Numbers
       print("Multiply and Divide (6, 3, 2):", multiply_and_divide(6, 3, 2))
       print("Modulus (10, 3):", modulus(10, 3))
       print("Power Operations (4):", power_operations(4))

       # Strings
       name = "John Doe"
       print_name(name)
       print("Split Name:", split_name(name))
       print("Case Conversion:", case_conversion(name))
       print("Reverse String:", reverse_string(name))

       # Lists
       food_list = create_food_list()
       print("Initial Food List:", food_list)
       updated_list = add_food_items(food_list, ["Sushi", "Steak"])
       print("After Adding Foods:", updated_list)
       removed_list = remove_food_item(updated_list, "Pizza")
       print("After Removing Pizza:", removed_list)
       print("Sorted Food List:", sort_food_list(removed_list))

3. Run the program and repeat the steps above until the output meets the above requirements.

4. Expected output <br/>
    ```Multiply and Divide (6, 3, 2): 9.0
    Modulus (10, 3): 1
    Power Operations (4): {'square': 16, 'cube': 64, 'pow_square': 16, 'pow_cube': 64}
    Full Name: John Doe
    Split Name: {'first_name': 'John', 'last_name': 'Doe'}
    Case Conversion: {'uppercase': 'JOHN DOE', 'lowercase': 'john doe'}
    Reverse String: eoD nhoJ
    Initial Food List: ['Pizza', 'Burger', 'Pasta', 'Ice Cream', 'Biryani']
    After Adding Foods: ['Pizza', 'Burger', 'Pasta', 'Ice Cream', 'Biryani', 'Sushi', 'Steak']
    After Removing Pizza: ['Burger', 'Pasta', 'Ice Cream', 'Biryani', 'Sushi', 'Steak']
    Sorted Food List: ['Biryani', 'Burger', 'Ice Cream', 'Pasta', 'Steak', 'Sushi']
    ```
    
5.  Run the unit testing program to ensure that your program runs as expected.
    For Linux and Mac users
    ```
    ./test.sh
    ```
       
    For windows users
    ```
    ./win_test.bat
    ```
       
    The unit testing will output the results of a series of tests using specific input and expected output.  Any error will provide information on where the expected output is different from the actual output.  You will need to edit your source code to fix the error and run `./test.sh` or `./win_test.bat` repeatedly until it passes all the test.

## Submission

Submit a zip file containing all the code files on canvas 

Naming Convention: CWID_LastName.zip  

Your zipped folder should contain below files:
```
CWID_LASTNAME.zip -
                  | > test.py
                  | > test.sh
                  | > assignment1.py
                  | > win_test.bat
```