from unittest import TestCase

from arr_algs import find_min
from arr_algs import find_average
from str_algs import revert_str
from dict_algs import find_children


class FindMinTests(TestCase):
    def test_find_min_range(self):
        arr = range(10)
        self.assertEqual(find_min(arr), 0)

    def test_find_min_generator(self):
        arr = (i for i in range(5))
        self.assertEqual(find_min(arr), 0)

    def test_find_min_random(self):
        arr = (10, 9, 1, 19, 1, 4, 5, 6, 8, -1, 11)
        self.assertEqual(find_min(arr), -1)

    def test_find_min_set(self):
        arr = {2, 3, 2, 5}
        self.assertEqual(find_min(arr), 2)

    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            find_min(1)
        with self.assertRaises(AssertionError):
            find_min(type)
        with self.assertRaises(TypeError):
            find_min([1, 2, 'v', '3'])
        with self.assertRaises(AssertionError):
            find_min('12345')


class FindAverageTests(TestCase):
    def test_find_average_eq_ok(self):
        arr = [1, 1, 1]
        self.assertEqual(find_average(arr), 1)

    def test_find_average_ok(self):
        arr = [1, 1, 1]
        self.assertEqual(find_average(arr), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            find_average('1111')
        with self.assertRaises(TypeError):
            find_average(1)
        with self.assertRaises(TypeError):
            find_average(type)


class RevertStrTest(TestCase):
    def test_revert_ok(self):
        s = '12345'
        self.assertEqual(revert_str(s), '54321')
        s = 'ab12чя'
        self.assertEqual(revert_str(s), 'яч21ba')

    def test_revert_invalid(self):
        with self.assertRaises(AssertionError):
            revert_str([1, 2, 3])
        with self.assertRaises(AssertionError):
            revert_str({1, 2, 3})
        with self.assertRaises(AssertionError):
            revert_str((1, 2, 3))
        with self.assertRaises(AssertionError):
            revert_str(type)


class FindChildrenTest(TestCase):
    def test_find_easy(self):
        emps = [
            {
                "name": "ivan",
                "age": 34,
                "children": [
                    {
                        "name": "vasja",
                        "age": 12,
                    },
                    {
                        "name": "petja",
                        "age": 10,
                    }
                ],
            },
            {
                "name": "darja",
                "age": 41,
                "children": [
                    {
                        "name": "kirill",
                        "age": 21,
                    },
                    {
                        "name": "pavel",
                        "age": 15,
                    },
                ],
            },
        ]
        res = ['darja']
        have_children = [i for i in find_children(emps)]
        self.assertEqual(len(have_children), len(res))
        self.assertEqual(have_children, res)

    def test_random_cases(self):
        emps = [
            {
                "name": "ivan",
                "age": 34,
                "children": [
                    {
                        "name": "vasja",
                        "age": 12,
                    },
                    {
                        "name": "petja",
                        "age": 10,
                    }
                ],
            },
            {
                "name": "darja",
                "age": 41,
                "children": [
                    {
                        "name": "kirill",
                        "age": 21,
                    },
                    {
                        "name": "pavel",
                        "age": 15,
                    },
                ],
            },
            {
                "name": "victor",
                "age": 23,
            },
            {
                "name": "ppp",
                "age": 41,
                "children": [
                    {
                        "name": "kirill",
                        "age": 41,
                    },
                    {
                        "name": "kirill 2",
                        "age": 41,
                    },
                    {
                        "name": "kirill 3",
                        "age": 41,
                    },
                ],
            },
        ]
        res = ['darja', 'ppp']
        have_children = [i for i in find_children(emps)]
        self.assertEqual(len(have_children), len(res))
        self.assertEqual(have_children, res)
