'''
Name: Kayla Ngo
Date: 09/17/2025
File Purpose: main driver file to run menu program
'''

from functions import *

def line():
    print("-" * 70)

if __name__ == "__main__":
    print("c. Dictionary Operations")
    line()

    # 1. create dictionary
    pairs = [("a", 1), ("b", 2), ("c", 3)]
    print ("1. create_dictionary from pairs:", pairs)
    cd = create_dictionary(pairs)
    print("create_dcitionary output: ", cd) 

    # 2. update dictionary
    d1 = {"x": 1}
    print("update_dictionary input:", d1, "update('x', '100)")
    print("output:", update_dictionary(d1, "x", 100))
    print("update_dictionary add new key 'y' with 2")
    print("output:", update_dictionary(d1, "y", 2))


    # 3. delete key
    d2 = {"m": 10, "n": 20}
    print("delete_key start dict:", d2)
    print("delete_key remove 'm'")
    print("output ", delete_key(d2, "m"))
    print("delete_key try removing missing key 'z'")
    try:
        delete_key(d2, "z")
    except KeyError as e:
        print("caught:", e)

    #4 dictionary comprehension example
    iterable = [2, 3.5, "cat", "go"]
    print("dict_comprehension_example input:", iterable)
    dce = dict_comprehension_example(iterable)
    print("output: ", dce)

    #5 merge dictionaries
    dicts = [{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 5}]
    print("merge_dictoinaries input:", dicts)
    md = merge_dictionaries(dicts)
    print("output: ", dicts)


    print("D. Looping Techniques")
    line()

    #6 iterate dictionary
    d3 = {"name": "Ana", "age": 30}
    print("iterate_dictionary input:", d3)
    id_out = iterate_dictionary(d3)
    print("output: ", id_out)

    #7 enumerate list
    colours = ["red", "green", "blue"]
    print("enumerate_list input:", colours)
    el_out = enumerate_list(colours)
    print("output: ", el_out)

    #8 zip lists
    lst1 = [1, 2, 3]
    lst2 = ["one", "two"]
    print("zip_lists inputs:", lst1, lst2)
    zl_out = zip_lists(lst1, lst2)
    print("output: ", zl_out)

    #9 reverse and sorted
    lst3 = [3, 1, 2]
    print("reverse_and_sort input:" , lst3)
    rev_list, sorted_list = reverse_and_sort(lst3)
    print("reversed:", rev_list)
    print("sorted:", sorted_list)

    print("E. Condition and Sequence Comparisons")
    line()

    seq = [1, 2, 3]
    print("Check_membership in", seq, "for 2:", check_membership (seq, 2))
    print("Check_membership in", seq, "for 4:", check_membership (seq, 4))

    print("chained comparison 1 < 2 == 2", chained_comparison(1, 2, 3))
    print("chained comparison 3 < 2 == 2", chained_comparison(1, 2, 3))

    print("boolean_evaluation True, False, False:", boolean_evaluation(True, False, False))
    print("boolean_evaluation 0, 0 'hello':", boolean_evaluation(0, 0, "hello"))

    print("compare_sequences [1, 2] vs [1, 2, 3]:", compare_sequences([1, 2], [1, 2, 3]))
    print("compare_sequences [1, 2, 3] vs [1, 2, 3]:", compare_sequences([1, 2, 3], [1, 2, 3]))
    print("compare_sequences [2] vs [1, 9]:", compare_sequences([2], [1, 9]))

    print("is_strictly_increasing [1, 2, 3]:", is_strictly_increasing([1, 2, 3]))
    print("is_strictly_increasing [1, 1, 2]:", is_strictly_increasing([1, 1, 2]))
    print("is_strictly_increasing [0, 0, 0]:", is_strictly_increasing([0, 0, 0]))