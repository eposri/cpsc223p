'''
Name: Kayla Ngo
Date: 10/01/2025
File Purpose: implemenation of queues 
'''

from collections import deque

today_sale = {}

def get_total_item(cart):
    '''
    takes in a positional arg dict 'cart'
    return the total price of all items in cart
    '''
    return sum(cart.values())


def checkout_queue(*args):
    '''
    takes in any numbers of positional args
    adds each name into a queue, first input will be added first
    return a queue of strings (use deque as return type)
    '''
    return deque(args)


def add_customer_cart(name, **kwargs):
    '''
    takes in one positional arg, 'name', and any number of keyword args
    no return needed
    '''
    today_sale[name] = kwargs
    print(f"Added {name} into today sale")


def lookup_cart(name):
    '''
    takes in one positional arg, 'name'
    looks up the cart in 'today_sale' based on given name
    prints out each item, their price, and total price
    '''
    if name in today_sale:
        cart = today_sale[name]
        print(f"{name}'s cart contains:")
        for item, price in cart.items():
            print(f"{item}: {price}")
        total = get_total_item(cart)
        print(f"Total price: {total}")    


def remove_item(name, item):
    '''
    takes in two pos args. 'name' (str) and 'item' (dict)
    look up an item and rm it from the customer's cart in 'today_sale'
    print a msg if item was removed
    print 'item not found' if item is not in cart
    '''
    if name in today_sale:
        if item in today_sale[name]:
            del today_sale[name][item]
            print(f"{item} has been removed from {name}'s cart")
        else:
            print(f'{item} not found')
    else:
        print(f"{name} not found in today's sale")


def apply_discount(name):
    '''
    takes in one positional args, 'name'
    applies 10% discount for each conditions met:
        - name length divisible by 3
        - first letter of name = vowel
        - name contains 2<= vowels
    print their name & respective discounts
    return discount percentage
    '''
    discount = 0
    if len(name) % 3 == 0:
        discount += 10
    if name[0].lower() in 'aeiou':
        discount += 10
    vowel_count = sum(1 for char in name.lower() if char in 'aieou')
    # use .lower on string every comparison 
    if vowel_count >= 2:
        discount += 10
    
    print(f"{name} gets a discount of {discount}%")
    return discount

def add_item(name, item, price=0):
    '''
    takes in two positional args
    add item into the customer's cart
        - if item has no price, set price to 0 -> print free
        - if name not found -> print
    '''
    if name in today_sale:
        today_sale[name][item] = price
    else:
        print(f"{name} not found")

def sale(queue):
    '''
    takes in deque object 'queue'
    pops from queue until empty
    prints current q state
        - look up name 'queue' for cart & total price (including) discount)
    print msg if q empty
    '''
    while queue:
        print(f"Current queue: {list(queue)}")
        name = queue[0]
        print(f"{name} is checking out")
        
        if name in today_sale:
            cart = today_sale[name]
            total = get_total_item(cart)
            discount_rate = apply_discount(name)
            
            if discount_rate > 0:
                discount_amount = total * (discount_rate/100)
                final_price = total - discount_amount
                print(f"Original price: {total}")
                print(f"Discount amount: {discount_amount}")
                print(f"Total price: {final_price}")
            else:
                print(f"Total price: {total}")

        else:
            print(f"{name} not found")
        queue.popleft()

    print("Queue is empty")