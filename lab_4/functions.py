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
    if not args:
        return ()
    return args


def unpack_tuple(t):
    """Unpack the tuple into individual variables and return them as a list."""
    l = list(t)
    return l


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
    d = dict(length=len(t))
    if t == ():
        return d
    else:
        d['first'] = t[0]
        d['last'] = t[-1]
        return d


### B. Set Operations
def create_set(iterable):
    """
    Create a set from the given iterable.
    """
    s = set(iterable)
    return s


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
    # union
    u = s1.union(s2)
    # intersection
    i = s1.intersection(s2)
    # difference
    d = s1.difference(s2)
    # symmetric difference
    s = s1.symmetric_difference(s2)
    return dict(union=u, intersection=i, difference=d, symmetric_difference=s)


def unique_sorted(iterable):
    """
    Return a sorted list of unique elements from the provided iterable.

    Arguments:
        iterable : An iterable that may contain duplicate elements.
    Return:
        A sorted list of the unique elements.
    """
    li = list(set(iterable))
    sorted_list = sorted(li)
    return sorted_list


### C. Stack and Queue Implementations
#### Stack
def push(stack, item):
    stack.append(item)


def pop(stack):
    """Remove and return the top item. Raise IndexError if empty."""
    if not stack:
        raise IndexError("Stack is empty: Index Error.")
    return stack.pop()


#### Queue
def enqueue(queue, item):
    queue.append(item)


def dequeue(queue):
    """Remove and return the front item. Raise IndexError if empty."""
    if not queue:
        raise IndexError("Queue is empty: Index Error.")
    return queue.pop(0)