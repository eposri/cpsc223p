from shopping import *

add_customer_cart('David', apple=10.0, egg=1.0, sushi=11.8)
add_customer_cart('John', banana=5.0, egg=1.0)
add_customer_cart('Alice', orange=3.0, milk=2.5)

line_up = checkout_queue('John', 'David', 'Alice')

print(line_up)

print(lookup_cart('John'))