'''
Name: Kayla Ngo
Date: 10/22/2025
'''

import os
import json

import functions

def main():
    file_name = "students.json"
    data = functions.load_data(file_name)
    
    while True:
        print("\n======= Student Records Menu =======")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Save and exit")

        choice = input("Enter option (1-3): ")

        if choice == '1':
            functions.add_student(data)
        elif choice == '2':
            functions.view_students(data)
        elif choice == '3':
            functions.save_data(data, file_name)
            return
        else:
            print("Invalid input. Please try again.")
            
if __name__ == "__main__":
    main()