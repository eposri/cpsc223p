
# Lab 5: Grocery Shopping


## Instruction:
1. Create a module `shopping.py` with the following functions:

    - Initialize an empty dictionary named `today_sale`

    - `get_total_item(cart)`: this function will take in a positional argument dictionary `cart`.  Return the total price of all items in `cart`. Example:
        
        `your_cart = {'banana'= 5.0, 'chicken' = 1.0}`
        `total = get_total_item(your_cart)`
        `print(your_cart)` 
        `**printing: 6.0**`

    `checkout_queue(...)`: this function will take in any numbers of positional arguments. You may assume each input is a string
    of name. This function will add each name into a queue, first input will be added first. Return a queue of string. Be sure to
    use deque as your return type. Example:

        `queue = checkout_queue('John','David','Hu')`
        `print(queue)`
        `**printing: deque(['John','David','Hu'])**`

    `add_customer_cart(name, ...)`: this function will take in one postional argument `name` and any number of keywords
    arguments. For each input positional arguments, you may assume it will be string name. For each input keyword arguments, you
    may assume it will be in the form of `food=price`.
    Print `This cart belongs to name` and add `name:{food:price,..}` into `today_sale`. No return is needed. Example:

        `add_customer_cart('John', pizza=5.0, chocolate=11.6)`
        `**printing: "Added John cart into today sale**`

    `lookup_cart(name)`: this function will take in one postional argument `name` and look up the cart in `today_sale` based on the given name. Print out each
    item, their  price, and total price. Make sure to implement `get_total_item()`

        `lookup_cart('John')`
        `**printing: "John cart contains:"**`
        `**pizza: 5.0**`
        `**chocolate: 11.6**`
        `**Total price: 16.6**`

    `remove_item(name, item)`: this function will take in two positional arguments `name` (string) and `item`(dictionary).
    Look up for the item and remove it from the customer's cart in `today_sale`. Print a message if item was removed. Print "item not found" if item is not in
    cart.

    `apply_discount(name)`: this function will take in one positional arguments `name`. Apply 10% discount for each conditions met if their name length is divisible by 3,
    the first letter of their names is a vowel, or if their names contain two or more vowels. Print out their name and the discount they get. Return the discount percentage.

    `add_item(name, item, price)`: this function will take in two positional arguments. Add the item into the customer's cart.
    If the item doesn't have any price, set the price to 0, and print a message to let them know the item is free. If name is not found, print "name not found" 
        
    `sale(queue)`: this function will take in a deque object. It will pop from `queue` until `queue` is empty. Print the current 
    queue and the name of the people who is about to check out before popping. Look up the name `queue` for their cart and total    
    price. Remember to apply discount to their cart if applicale. Print a message if queue is empty.
