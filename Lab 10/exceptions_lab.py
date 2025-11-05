'''
Name: Kayla Ngo
Date: 10/29/2025
'''

def divide_numbers(*, numerator, denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    # can return result here as well
# print(divide_numbers(numerator=6,denominator=2))
    
def parse_int(*, value):
    try:
        return int(value)
    except ValueError:
        return "Error: Invalid integer"
# parse_int(value="123")
# parse_int(value="abc") will return err msg

class NegativeValueError(Exception):
    pass

def custom_exception_demo(*, value):
    if value < 0:
        raise NegativeValueError(f"Negative values are not allowed")
    return value
    
def chain_exception_demo(*, filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise Exception("Chained Exception: File operation failed")
    
def cleanup_demo(*, filename):
    file_handle = None
    try:
        file_handle = open(filename, 'w')
        file_handle.write("Hello Mars!")
    except FileNotFoundError as e:
        raise Exception("File not found")
    finally:
        if file_handle:
            file_handle.close()
        print("Cleanup complete")

def type_error_demo(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Incompatible types for addition"
