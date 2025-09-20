'''
Name: Kayla Ngo
Date: 9/14/2025
Purpose of File: Python program that performs as a Tuffy Titan 
                 Contact List, which contains a list of contacts
                 that can be modified or deleted
'''

def add_contact(contact_list, *, first_name, last_name):
    '''Add a contact to the list in the form of ["first name", "last name"]'''
    contact_list.append([first_name, last_name])

def modify_contact(contact_list, *, first_name, last_name, index):
    '''
    Case I: If the index it is within the range of the contact list, modify
            the appropriate index of the contact list with the 
            first_name/last_name contact, and return a True.
    Case II: If the index it is not within the range of the contact list,
             return a False without modifying the contact list.
    '''
    if 0 <= index < len(contact_list):
        contact_list[index] = [first_name, last_name]
        return True
    else:
        return False

def delete_contact(contact_list, *, index):
    '''
    Case I: If the index it is within the range of the contact list, delete
            the contact at the index value, and return a True.
    Case II: If the index it is not within the range of the contact list, 
             return a False without modifying the contact list.
    '''
    if 0 <= index < len(contact_list):
        contact_list.remove(contact_list[index])
        return True
    else:
        return False

def sort_contacts(contact_list, *, column):
    '''
    Case I: If the column is 0, sort the contact list by first name.
    Case II: If the column is 1, sort the contact list by last name.
    '''
    if column == 0:
        return contact_list.sort(key=lambda contact: contact[0])
    elif column == 1:
        return contact_list.sort(key=lambda contact: contact[1])