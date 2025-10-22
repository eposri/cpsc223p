'''
Name: Kayla Ngo
Date: 10/22/2025
'''

from shapes.circle import area as circle_area, circumference as circle_circumference
from shapes.rectangle import area as rect_area, perimeter as rect_perimeter
from shapes.triangle import area as tri_area, perimeter as tri_perimeter

def main():
    print("Welcome to the Shapes Program!")
    shape = input("Choose a shape (circle, rectangle, triangle):").strip().lower()

    if shape == "circle":
        radius = float(input("Enter the radius:"))
        print(f"Area: {circle_area(radius)}")
        print(f"Circumference: {circle_circumference(radius)}")
    elif shape == "rectangle":
        length = float(input("Enter the length:"))
        width = float(input("Enter the width:"))
        print(f"Area: {rect_area(length, width)}")
        print(f"Perimeter: {rect_perimeter(length, width)}")
    elif shape == "triangle":
        base = float(input("Enter the base:"))
        height = float(input("Enter the height:"))
        side1 = float(input("Enter the first side:"))
        side2 = float(input("Enter the second side:"))
        side3 = float(input("Enter the third side:"))
        print(f'Area: {tri_area(base, height)}')
        print(f'Perimeter: {tri_perimeter(side1, side2, side3)}')
    else:
        print("Invalid shape!" \
              "Please enter one of the following: circle, rectangle, triangle")
        return
    
if __name__ == "__main__":
    main()