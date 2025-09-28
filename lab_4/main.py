'''
Name: Kayla Ngo
Date: 09/17/2025
File Purpose: Main driver file to run menu program
'''

from functions import *


def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def parse_input(prompt):
    raw = input(prompt).strip()
    if not raw:
        return []
    parts = raw.split(",")
    result = []
    for x in parts:
        result.append(x.strip())
    return result


def menu():
    print("Choose an option:")
    print("1. Tuple Operations")
    print("2. Set Operations")
    print("3. Stack Operations")
    print("4. Queue Operations")
    print("5. Exit")
    choice = input("Enter 1-5:" ).strip()
    return choice


def tuple_menu():
    print_header("Tuple")
    items = parse_input("Enter items for tuple (comma separated): ")
    t = create_tuple(*items)
    print(f"\nCreated tuple: {t}")

    unpacked = unpack_tuple(t)
    print(f"\nUnpacked to List: ", unpacked)

    details = tuple_details(t)
    print(f"\nTuple details: ", details) 


def set_menu():
    print_header("Set Operations")
    a_items = parse_input("Enter items for Set A (comma separated): ")
    b_items = parse_input("Enter items for Set B (comma separated): ")

    set_a = create_set(a_items)
    set_b = create_set(b_items)

    print(f"\nSet A: {set_a}")
    print(f"\nSet B: {set_b}")

    results = set_operations(set_a, set_b)
    print("\nResults: ")
    print("Union: ", results["union"])
    print("Intersection: ", results["intersection"])
    print("Difference: ", results["difference"])
    print("Symmetric Difference: ", results["symmetric_difference"])

    merger_unique_sorted = unique_sorted(a_items + b_items)
    print("\nUnique sorted: ", merger_unique_sorted)


def stack_menu(stack):
    while True:
        print_header("Stack Operations (LIFO)")
        print("a) Push")
        print("b) Pop")
        print("c) Back to main menu")
        choice = input("Enter a, b, or c: ").strip().lower()

        if choice == "a":
            item = input("Enter items to push: ").strip()
            push(stack, item)
            print(f"Pushed '{item}'.")
        elif choice == "b":
            try: 
                item = pop(stack)
                print(f"Popped '{item}'.")
            except IndexError:
                print("The stack is empty, nothing to pop.")
        elif choice == "c":
            return
        else:
            print("Please enter a valid option.")


def queue_menu(queue):
    while True:
        print_header("Queue Operations (FIFO)")
        print(f"Current queue: {queue}")
        print("a) Enqueue")
        print("b) Dequeue")
        print("c) Back to main menu")
        choice = input("Enter a, b, or c: ").strip().lower()

        if choice == "a":
            item = input("Enter items to enqueue: ").strip()
            enqueue(queue, item)
            print(f"Enqueued '{item}'.")
        elif choice == "b":
            try: 
                item = dequeue(queue)
                print(f"Dequeued '{item}'.")
            except IndexError:
                print("The qeueue is empty, nothing to dequeue.")
        elif choice == "c":
            return
        else:
            print("Please enter a valid option.")


def main():
    current_stack = []
    current_queue = []

    while True:
        choice = menu()
        if choice == "1":
            tuple_menu()
        elif choice == "2":
            set_menu()
        elif choice == "3":
            stack_menu(current_stack)
        elif choice == "4":
            queue_menu(current_queue)
        elif choice == "5":
            print("\nGoodbye.")
            break
        else:
            print("\nPlease enter a valid option.")


if __name__ == "__main__":
    main()