'''
Name: Kayla Ngo
Date: 10/22/2025
'''

import os
import json

def load_data(filename):
    '''
    loads student data from a JSON file
    if the file DNE, returns empty list
    '''
    if not os.path.exists(filename):
        return []
    
    try:
        with open(filename, 'r') as f:
            student_data = json.load(f)
            return student_data
    # if not raise error json.JSONDecodeError(msg,doc,pos)
    # <https://docs.python.org/3.14/library/json.html>
    except json.JSONDecodeError:
        return []
    
def save_data(data, filename):
    '''
    saves student data to JSON file
    '''
    with open(filename, 'w') as f:
        json.dump(data, f)
        
    

def add_student(data):
    '''
    adds a new student record to the list after taking input
    from the user
    '''
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    
    new_student = {
        "name": name,
        "age": age
    }

    data.append(new_student)
    return data

def view_students(data):
    '''
    displays all student records in a readable format
    '''
    if not data:
        print('No students found.')
    else:
        print("Student Records:")
        for idx, student in enumerate(data, start=1):
            print(f"{idx}. Name: {student['name']}, Age: {student['age']}")
        #for student in data:
            #print(f"Name: {student['name']}, Age: {student['age']}")
            #print(f"   Age: {student['age']}")