# Lab 4: Tuples, Sets, Stacks, and Queues in Python

Welcome to this lab. You will practise core Python data structures and write clean, testable code. By the end, you will have a small menu-driven program, a module with functions, and unit tests that prove your code works.

## Learning outcomes

* Work with tuples 
* Use sets for common operations
* Implement a stack and a queue with Python lists
* Build a simple menu-driven program
* Write and run unit tests

## What you will build

* `functions.py` holds all logic
* `main.py` is a menu-driven driver that imports and uses `functions.py`
* `test.py` checks your functions with unit tests

## Repository layout

```
.
├── main.py          # Driver program with the text menu
├── functions.py     # All required functions live here
├── test.py          # Unit tests for automated checking
└── README.md        # This file
```

## Setup

* Python 3.9 or later
* No third-party packages are required


---

## Tasks and specifications

Put the following functions in `functions.py`. Use the exact names and signatures.

### A. Tuples

```python
def create_tuple(*args):
    """Pack the provided arguments into a tuple and return it."""
    # Your code here


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
```


### B. Set Operations

```python
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
```



### C. Stack and Queue Implementations

Use Python lists to model both structures.

#### Stack

* Push
* Pop

Provide two helper functions in `functions.py`:

```python
def push(stack, item):
    # Your code here


def pop(stack):
    """Remove and return the top item. Raise IndexError if empty."""
    # Your code here
```

#### Queue

* Enqueue: add at the end
* Dequeue: remove from the front

Provide two helper functions:

```python
def enqueue(queue, item):
    # Your code here


def dequeue(queue):
    """Remove and return the front item. Raise IndexError if empty."""
    # Your code here
```

Note: `pop(0)` is O(n) which is fine for this lab. For larger data, `collections.deque` is better.


## Driver program requirements (`main.py`)

Write a text menu that loops until the user chooses to quit. Import and call functions from `functions.py`. Your menu should support these options:

1. Tuple 
2. Set operations
3. Stack operations, push and pop
4. Queue operations, enqueue and dequeue
5. Exit

Design guidance:

* Print clear prompts and results
* Keep state where helpful, for example a current stack or queue in memory
* Validate input, handle empty structures with friendly messages


## How to run

Run the program:

```bash
python3 main.py
```

Run the tests with `unittest`:

```bash
python3 -m unittest -v
```


## Common pitfalls

* Forgetting to include `first` and `last` only for non-empty tuples
* Returning lists from set functions rather than sets
* Catching exceptions too broadly, prefer `IndexError` for empty pops and dequeues

## Academic integrity

Write your own code. You may discuss ideas with classmates, but the code you submit must be your own.

Happy coding!

## Submission Instructions
Zip this __folder__ and name it as CWID_Last_Name.zip and submit it timely on canvas.

Convert the above into a better assignment especially the tasks of tuples, stack and queue