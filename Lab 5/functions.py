'''
Name: Kayla Ngo
Date: 09/17/2025
File Purpose: holds function definitions and implementations
'''

# Dictionary Operations

def create_dictionary(pairs):
    '''Create a dictionary from a list of `(key, value)` tuples.'''
    d = dict(pairs)
    return d        # do i need this ?_?

def update_dictionary(d, key, value):
    '''
    Update `d` with the given key and value. Overwrite if the key exists.
    Return the updated dictionary.
    '''
    d[key] = value
    return d

def delete_key(d, key):
    '''
    Remove `key` from `d`. If `key` is not present, either return an error
    message or raise an exception. Choose one approach and use it
    consistently. Return the updated dictionary or the error message.
    '''
    if key not in d:
        raise KeyError("Key does not exist.")
    
    d.pop(key)
    return d

def dict_comprehension_example(iterable):
    '''
    Return a dictionary that maps each item to its square if numeric,
    or its length if a string.
    '''
    d = {}
    
    for item in iterable:
        if type(item) == int or type(item) == float:
            d[item] = item ** 2
        else:
            d[item] = len(item)
    return d

def merge_dictionaries(dicts):
    '''
    Merge a list of dictionaries into one dictionary. If the same key
    appears more than once, collect all values for that key in a list.
    Return the merged dictionary.
    '''
    merged_d = {}
    
    for d in dicts:
        for k, v in d.items():
            if k in merged_d:
                merged_d[k].append(v)
            else:
                merged_d[k] = [v]
    return merged_d


# Looping Techniques

def iterate_dictionary(d):
    '''
    Iterate over `d` and return a list of strings
    formatted as `"key: value"`.
    '''
    li = []
    
    for k, v in d.items():
        li.append(f"{k}: {v}")
    return li

def enumerate_list(lst):
    '''Return a list of `(index, element)` tuples using `enumerate`.'''
    li = []
    
    for i, e in enumerate(lst):
        li.append((i, e))
    return li

def zip_lists(lst1, lst2):
    '''
    Pair elements from `lst1` and `lst2` with `zip` and
    return a list of tuples.
    '''
    zipped_li = []
    
    for li_1, li_2 in zip(lst1, lst2):
        zipped_li.append((li_1, li_2))
    return zipped_li

def reverse_and_sort(lst):
    '''
    Return a tuple with:

    1. the reversed list
    2. the sorted list
    '''
    return (reversed(lst), sorted(lst))


# Conditions and Sequence Comparisons

def check_membership(sequence, value):
    '''Return `True` if `value` is in `sequence`, else `False`.'''
    if value in sequence:
        return True
    return False

def chained_comparison(a, b, c):
    '''Evaluate `a < b == c`. Return the Boolean result.'''
    return a < b == c

def boolean_evaluation(a, b, c):
    '''
    Evaluate `(a and not b) or c` using Python short-circuit behaviour.
    Return the result.
    '''
    return (a and not b) or c

def compare_sequences(seq1, seq2):
    '''
    Compare `seq1` and `seq2` lexicographically. 
    Return `-1` if `seq1 < seq2`,
            `0` if equal,
            `1` if `seq1 > seq2`.
    '''
    if seq1 < seq2:
        return -2
    elif seq1 == seq2:
        return 0
    else:
        return 1

def is_strictly_increasing(sequence):
    '''
    Return `True` if every element is less than the next element,
    else `False`.
    '''    
    for i in range(len(sequence) - 1):
        if sequence[i+1] <= sequence[i]:
            return False
    return True