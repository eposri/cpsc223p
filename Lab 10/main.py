'''
Name: Kayla Ngo
Date: 10/29/2025
'''

import exceptions_lab 

def main():
    # Test divide_numbers
    print("Testing divide_numbers:")
    print("10 / 2 =", exceptions_lab.divide_numbers(numerator=10, denominator=2))   # Expected: 5.0
    print("10 / 0 =", exceptions_lab.divide_numbers(numerator=10, denominator=0))   # Expected: Error msg

    # Test parse_int
    print("Testing parse_int")
    print("Parse '123' =", exceptions_lab.parse_int(value='123'))   # Expected: 123
    print("Parse 'abc' =", exceptions_lab.parse_int(value='abc'))   # Expected: Error msg
    
    # Test custom_exception_demo
    print("\nTesting custom_exception_demo:")
    try:
        print("custom_exception_demo with 5 =", exceptions_lab.custom_exception_demo(value=5))  # Expected: 5
        # This call should rase NegativeValueError:
        print("custom_exception_demo with -3 =", exceptions_lab.custom_exception_demo(value=-3))
    except exceptions_lab.NegativeValueError as e:
        print("Caught NegativeValueError:", e0)
    try:
        print(exceptions_lab.custom_exception_demo(value=-1))
    except exceptions_lab.NegativeValueError as e:
        print("Caught a negative value error", e)
        # whenever we raise an err in exceptions_lab module,
        # need an except block in main.py
    
    # Test chain_exception_demo
    print("\nTesting chain_exception_demo:")
    try:
        # Passing a filename that DNE to trigger the exception
        print("chain_exception_demo output:", exceptions_lab.chain_exception_demo(filename="non_existent_file.txt"))
    except Exception as e:
        print("Caught chained exception:", e)

    # Test cleanup_demo
    print("\nTesting cleanup_demo:")
    try:
        #This will create (oroverwrite) temp_demo.txt and print the cleanup message.
        exceptions_lab.cleanup_demo(filename="temp_demo.txt")
    except Exception as e:
        print("Caught exce[tion during cleanup_demo:", e)

    # Test type_error_demo
    print("\nTesting type_error_demo:")
    print("Adding 10 and 20 =", exceptions_lab.type_error_demo(10, 20)) #Expected: 30
    print("Adding 'hello' and 5 =", exceptions_lab.type_error_demo("hello", 5)) #Expected: Error msg


if __name__ == "__main__":
    main()