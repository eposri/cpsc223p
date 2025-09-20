# test.py

import unittest
from functions import (
    create_tuple,
    unpack_tuple,
    tuple_details,
    create_set,
    set_operations,
    unique_sorted,
    push,
    pop,
    enqueue,
    dequeue,
)


class TestTuplesAndSequences(unittest.TestCase):
    def test_create_tuple_empty(self):
        self.assertEqual(create_tuple(), ())

    def test_create_tuple_values(self):
        self.assertEqual(create_tuple(1, 2, "a"), (1, 2, "a"))

    def test_unpack_tuple_empty(self):
        self.assertEqual(unpack_tuple(()), [])

    def test_unpack_tuple_values(self):
        self.assertEqual(unpack_tuple((1, "x", 3)), [1, "x", 3])

    def test_tuple_details_empty(self):
        self.assertEqual(tuple_details(()), {"length": 0})

    def test_tuple_details_non_empty(self):
        t = (10, 20, 30)
        self.assertEqual(
            tuple_details(t),
            {"length": 3, "first": 10, "last": 30},
        )


class TestSetOperations(unittest.TestCase):
    def test_create_set_empty(self):
        self.assertEqual(create_set([]), set())

    def test_create_set_values(self):
        self.assertEqual(create_set([1, 2, 2, 3]), {1, 2, 3})

    def test_unique_sorted_empty(self):
        self.assertEqual(unique_sorted([]), [])

    def test_unique_sorted_numbers(self):
        self.assertEqual(unique_sorted([3, 1, 2, 3, 2]), [1, 2, 3])

    def test_unique_sorted_strings(self):
        self.assertEqual(unique_sorted(["b", "a", "b"]), ["a", "b"])

    def test_set_operations_basic(self):
        a = {1, 2, 3}
        b = {3, 4, 5}
        result = set_operations(a, b)
        self.assertEqual(result["union"], {1, 2, 3, 4, 5})
        self.assertEqual(result["intersection"], {3})
        self.assertEqual(result["difference"], {1, 2})
        self.assertEqual(result["symmetric_difference"], {1, 2, 4, 5})

    def test_set_operations_do_not_mutate_inputs(self):
        a = {1, 2, 3}
        b = {3, 4}
        _ = set_operations(a, b)
        self.assertEqual(a, {1, 2, 3})
        self.assertEqual(b, {3, 4})


class TestStack(unittest.TestCase):
    def test_push_then_pop(self):
        stk = []
        push(stk, "x")
        push(stk, "y")
        self.assertEqual(pop(stk), "y")
        self.assertEqual(pop(stk), "x")
        self.assertEqual(stk, [])

    def test_pop_empty_raises(self):
        with self.assertRaises(IndexError):
            pop([])

    def test_push_mutates_in_place(self):
        stk = []
        push(stk, 1)
        self.assertEqual(stk, [1])


class TestQueue(unittest.TestCase):
    def test_enqueue_then_dequeue(self):
        q = []
        enqueue(q, "a")
        enqueue(q, "b")
        self.assertEqual(dequeue(q), "a")
        self.assertEqual(dequeue(q), "b")
        self.assertEqual(q, [])

    def test_dequeue_empty_raises(self):
        with self.assertRaises(IndexError):
            dequeue([])

    def test_enqueue_mutates_in_place(self):
        q = []
        enqueue(q, 10)
        self.assertEqual(q, [10])


if __name__ == "__main__":
    unittest.main()
