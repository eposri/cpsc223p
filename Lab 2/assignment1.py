'''
      Name: Kayla Ngo
      Date: 09/03/2025
      File Purpose: Demonstrates numbers, strings, and list operations
'''

# Numbers
def multiply_and_divide(a, b, c):
    return a * b / c

def modulus(a, b):
    return a % b

def power_operations(num):
    x = num ** 2
    y = num ** 3
    z = pow(num, 2)
    a = pow(num, 3)
    z = {"square": x, "cube": y, "pow_square": z, "pow_cube": a}
    return z

# Strings
def print_name(name):
    return print(name)

def split_name(name):
    li = name.split(" ")
    if len(li) == 2:
        dict = {"first_name": li[0], "last_name": li[1]}
        return dict
    else:
        dict = {"first_name": li[0], "last_name": ""}
        return dict

def case_conversion(name):
    upper = name.upper()
    lower = name.lower()
    x = {"uppercase": upper, "lowercase": lower}
    return x

def reverse_string(name):
    return name[::-1]

# Lists
def create_food_list():
    fave_foods = ["Plum", "Pasta", "Strawberry", "Pho", "Orange"]
    return fave_foods

def add_food_items(food_list, items):
    for item in items:
        food_list.append(item)
    return food_list

def remove_food_item(food_list, item):
    if item in food_list:
        food_list.remove(item)
    return food_list

def sort_food_list(food_list):
    sorted_list = sorted(food_list)
    return sorted_list
        


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