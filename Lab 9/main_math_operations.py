'''
Name: Kayla Ngo
Date: 10/22/2025
'''
import math_operations

def main():
    print("Welcome to the Math Operations Program!")

    try:
        print("\n======= Math Operations Menu =======")
        print("Add")
        print("Subtract")
        print("Multiply")
        print("Divide")
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
        choice = input("Enter operation choice:").strip().lower()

        if choice == 'add':
            result = math_operations.add(x, y)
        elif choice == 'subtract':
            result = math_operations.subtract(x, y)
        elif choice == 'multiply':
            result = math_operations.multiply(x, y)
        elif choice == 'divide':
            result = math_operations.divide(x, y)
        else:
            print("Invalid operation!" \
            "Please enter one of the following: add, subtract, multiply, divide")
            return
        
        if result is not None:
            print(f"The result of {choice}ing {x} on {y} is {result}.")
        else:
            print("Cannot divide by zero!")
    
    except ValueError:
        print("Invalid input! Please enter number.")

if __name__ == "__main__":
    main()