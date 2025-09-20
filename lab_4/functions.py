'''
Name: Kayla Ngo
Date: 09/17/2025
File Purpose: Demonstrates tuples, sets, stacks, and queues
'''


### A. Tuples
def create_tuple(*args):
    # *args = (1, 2, 3)
    # args = ([1, 2, 3])
    """Pack the provided arguments into a tuple and return it."""
    tup = (args)
    return tup


def unpack_tuple(t):
    """Unpack the tuple into individual variables and return them as a list."""
    # Your code here
    



def tuple_details(t):
    """
    Return a dictionary with details about the tuple. Include keys:
    - 'length' for the number of items
    - 'first' and 'last' only when the tuple is not empty

    Arguments:
        t : A tuple whose details are to be extracted.
    Return:
        A dictionary with keys such as 'length', 'first', and 'last'.
    """
    # Your code here


### B. Set Operations
def create_set(iterable):
    """
    Create a set from the given iterable.
    """
    # Your code here


def set_operations(s1, s2):
    """
    Given two sets, perform various set operations and return the results in a dictionary.

    Arguments:
        s1 : The first set.
        s2 : The second set.
    Return:
        A dictionary with the following keys:
        - 'union' : The union of s1 and s2.
        - 'intersection' : The intersection of s1 and s2.
        - 'difference' : The difference (elements in s1 but not in s2).
        - 'symmetric_difference': The symmetric difference of s1 and s2.
    """
    # Your code here


def unique_sorted(iterable):
    """
    Return a sorted list of unique elements from the provided iterable.

    Arguments:
        iterable : An iterable that may contain duplicate elements.
    Return:
        A sorted list of the unique elements.
    """
    # Your code here


### C. Stack and Queue Implementations
#### Stack
def push(stack, item):
    # Your code here


def pop(stack):
    """Remove and return the top item. Raise IndexError if empty."""
    # Your code here


#### Queue
def enqueue(queue, item):
    # Your code here


def dequeue(queue):
    """Remove and return the front item. Raise IndexError if empty."""
    # Your code here