import unittest
from functions import *


class TestDictionaryOperations(unittest.TestCase):
    def test_create_dictionary(self):
        pairs = [("a", 1), ("b", 2)]
        self.assertEqual(create_dictionary(pairs), {"a": 1, "b": 2})

    def test_update_dictionary_overwrite_and_add(self):
        d = {"x": 1}
        self.assertEqual(update_dictionary(d, "x", 100), {"x": 100})
        self.assertEqual(update_dictionary(d, "y", 2), {"x": 100, "y": 2})

    def test_delete_key_success(self):
        d = {"m": 10, "n": 20}
        out = delete_key(d, "m")
        self.assertEqual(out, {"n": 20})
        self.assertNotIn("m", out)

    def test_delete_key_missing_raises(self):
        d = {"m": 10}
        with self.assertRaises(KeyError):
            delete_key(d, "z")

    def test_dict_comprehension_example_numbers_and_strings(self):
        inp = [2, 3.5, "cat", "go"]
        out = dict_comprehension_example(inp)
        expected = {2: 4, 3.5: 12.25, "cat": 3, "go": 2}
        self.assertEqual(out, expected)

    def test_merge_dictionaries(self):
        dicts = [{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 5}]
        out = merge_dictionaries(dicts)
        self.assertEqual(out, {"a": [1, 5], "b": [2, 3], "c": [4]})


class TestLoopingTechniques(unittest.TestCase):
    def test_iterate_dictionary(self):
        d = {"name": "Ana", "age": 30}
        out = iterate_dictionary(d)
        # Order is not guaranteed; compare as sets
        self.assertEqual(set(out), {"name: Ana", "age: 30"})

    def test_enumerate_list(self):
        colours = ["red", "green", "blue"]
        out = enumerate_list(colours)
        self.assertEqual(out, [(0, "red"), (1, "green"), (2, "blue")])

    def test_zip_lists(self):
        lst1 = [1, 2, 3]
        lst2 = ["one", "two"]
        out = zip_lists(lst1, lst2)
        self.assertEqual(out, [(1, "one"), (2, "two")])

    def test_reverse_and_sort(self):
        lst = [3, 1, 2]
        rev_out, sort_out = reverse_and_sort(lst)
        self.assertEqual(rev_out, [2, 1, 3])
        self.assertEqual(sort_out, [1, 2, 3])


class TestConditionsAndComparisons(unittest.TestCase):
    def test_check_membership(self):
        seq = [1, 2, 3]
        self.assertTrue(check_membership(seq, 2))
        self.assertFalse(check_membership(seq, 4))

    def test_chained_comparison(self):
        self.assertTrue(chained_comparison(1, 2, 2))
        self.assertFalse(chained_comparison(3, 2, 2))
        self.assertFalse(chained_comparison(1, 2, 3))

    def test_boolean_evaluation(self):
        self.assertTrue(boolean_evaluation(True, False, False))
        self.assertEqual(boolean_evaluation(0, 0, "hello"), "hello")
        self.assertFalse(boolean_evaluation(False, True, 0))

    def test_compare_sequences(self):
        self.assertEqual(compare_sequences([1, 2], [1, 2, 3]), -1)
        self.assertEqual(compare_sequences([1, 2, 3], [1, 2, 3]), 0)
        self.assertEqual(compare_sequences([2], [1, 9]), 1)

    def test_is_strictly_increasing(self):
        self.assertTrue(is_strictly_increasing([1, 2, 3]))
        self.assertFalse(is_strictly_increasing([1, 1, 2]))
        self.assertFalse(is_strictly_increasing([0, 0, 0]))
        self.assertTrue(is_strictly_increasing((-5, -2, 0, 10)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
