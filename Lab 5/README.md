# Lab 5

Advanced Data Structures, Looping Techniques, and Enhanced Dictionary Operations in Python

## 1. Overview

Build a small Python programme that exercises:

* **Dictionaries**: creating, updating, deleting, merging, and dictionary comprehensions
* **Looping techniques**: `dict.items()`, `enumerate`, `zip`, reverse order, and sorted order
* **Conditions and comparisons**: membership, chained comparisons, Boolean logic with short-circuit behaviour, and lexicographical ordering

You will implement functions in `functions.py`, write demonstration tests in `main.py`, and run the **provided** unit tests using `unittest`.

---

## 2. What you will create

```
|-- functions.py
|-- main.py
|-- test.py
```

### Provided to you

```
test.py   # Do not modify. You only need to run it via unittest.
```

---

## 3. `functions.py`

At the very top of the file include your **name**, **date**, and a brief **purpose** comment.

### 3.1 Dictionary Operations

**1) `create_dictionary(pairs)`**
Create a dictionary from a list of `(key, value)` tuples.

**2) `update_dictionary(d, key, value)`**
Update `d` with the given key and value. Overwrite if the key exists. Return the updated dictionary.

**3) `delete_key(d, key)`**
Remove `key` from `d`. If `key` is not present, either return an error message or raise an exception. Choose one approach and use it consistently. Return the updated dictionary or the error message.

**4) `dict_comprehension_example(iterable)`**
Return a dictionary that maps each item to its square if numeric, or its length if a string.

**5) `merge_dictionaries(dicts)`**
Merge a list of dictionaries into one dictionary. If the same key appears more than once, collect all values for that key in a list. Return the merged dictionary.

### 3.2 Looping Techniques

**6) `iterate_dictionary(d)`**
Iterate over `d` and return a list of strings formatted as `"key: value"`.

**7) `enumerate_list(lst)`**
Return a list of `(index, element)` tuples using `enumerate`.

**8) `zip_lists(lst1, lst2)`**
Pair elements from `lst1` and `lst2` with `zip` and return a list of tuples.

**9) `reverse_and_sort(lst)`**
Return a tuple with:

1. the reversed list
2. the sorted list

### 3.3 Conditions and Sequence Comparisons

**10) `check_membership(sequence, value)`**
Return `True` if `value` is in `sequence`, else `False`.

**11) `chained_comparison(a, b, c)`**
Evaluate `a < b == c`. Return the Boolean result.

**12) `boolean_evaluation(a, b, c)`**
Evaluate `(a and not b) or c` using Python short-circuit behaviour. Return the result.

**13) `compare_sequences(seq1, seq2)`**
Compare `seq1` and `seq2` lexicographically. Return `-1` if `seq1 < seq2`, `0` if equal, `1` if `seq1 > seq2`.

**14) `is_strictly_increasing(sequence)`**
Return `True` if every element is less than the next element, else `False`.

---

## 4. `main.py` (driver)

At the very top include your **name**, **date**, and a brief **purpose** comment.

* **Import** all functions from `functions.py`
* **Execution block** so your demos run only when the file is executed directly:

```python
if __name__ == "__main__":
    # Call each function with sample inputs
    # Print the inputs and outputs
    # Include brief comments for expected results
    pass
```

---

## 5. Run the programme

Run the driver:

```bash
python3 main.py
```

Run the tests with `unittest`:

```bash
python3 -m unittest -v
```

---

## 6. Submission

Create a zip using the naming convention:

```
CWID_LastName_Firstname.zip
```

Your zip must contain:

```
functions.py
main.py
test.py
README.md
```

Submit the zip on Canvas.

---

## 7. Marking scheme

All points add up to **100**.

| Points | Description                          |
| -----: | ------------------------------------ |
|     50 | Environment setup and lab submission |
|     20 | All required files submitted on time |
|     30 | All unit tests passed                |

Partial credit will be awarded where appropriate.
