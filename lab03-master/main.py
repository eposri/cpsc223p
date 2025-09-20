'''
Name: Kayla Ngo
Date: 9/14/2025
Purpose of File: Python program that performs as a Tuffy Titan 
                 Contact List, which contains a list of contacts
                 that can be modified or deleted
'''

import contacts

def main():
    contact_list = []

    while True:
        print("*** TUFFY TITAN CONTACT MAIN MENU")
        print("""
        1. Print list
        2. Add contact
        3. Modify contact
        4. Delete contact
        5. Sort list by first name
        6. Sort list by last name
        7. Exit the program
        """)

        menu_choice = input("Enter menu choice: ").strip()

        if menu_choice == '1':
            print("================== CONTACT LIST ==================")
            print("Index   First Name            Last Name")
            print("======  ====================  ====================")

            for idx, (first_name, last_name) in enumerate(contact_list):
                print(f"     {idx:<7} {first_name:<21} {last_name:<20}")

        elif menu_choice == '2':
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()
            contacts.add_contact(contact_list,
                                 first_name=first_name,
                                 last_name=last_name)

        elif menu_choice == '3':
            first_name = input("Enter first name: ").strip()
            last_name = input("Enter last name: ").strip()
            idx = input("Enter index number: ").strip()
            contacts.modify_contact(contact_list,
                                    first_name=first_name,
                                    last_name=last_name,
                                    index=int(idx))

        elif menu_choice == '4':
            idx = input("Enter index number: ").strip()
            contacts.delete_contact(contact_list, index=int(idx))

        elif menu_choice == '5':
            contacts.sort_contacts(contact_list, column=0)

        elif menu_choice == '6':
            contacts.sort_contacts(contact_list, column=1)

        else:
            break

if __name__ == "__main__":
    main()