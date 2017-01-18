#!/usr/bin/env python3

from types import GeneratorType
from unittest import TestCase

from librip.gens import field
from librip.gens import gen_random
from librip.iterators import Unique


class TestFields(TestCase):
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    ]

    def test_invalid_params(self):
        with self.assertRaises(AssertionError):
            r = [i for i in field(self.goods)]

    def test_invalid_params_but_not_called(self):
        field(self.goods)

    def test_one(self):
        data = ['Ковер', 'Диван для отдыха']
        resp = [i for i in field(self.goods, 'title')]
        self.assertEqual(len(resp), len(data))
        self.assertEqual(resp, data)

    def test_empty(self):
        resp = [i for i in field(self.goods, 'non-existent-field')]
        self.assertEqual(len(resp), 0)

    def test_multi_args(self):
        resp = [i for i in field(self.goods, 'price', 'color')]
        self.assertEqual(len(resp), 2)
        for item in resp:
            self.assertIn('price', item)
            self.assertIn('color', item)
            self.assertEqual(len(item), 2)

    def test_multi_args_with_one_empty(self):
        resp = [i for i in field(self.goods, 'price', 'color', 'non-existent-field')]
        self.assertEqual(len(resp), 2)
        for item in resp:
            self.assertIn('price', item)
            self.assertIn('color', item)
            self.assertNotIn('non-existent-field', item)
            self.assertEqual(len(item), 2)

    def test_multi_args_all_empty(self):
        goods = [
            {'title': 'Ковер', 'price': 2000, 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        ]
        resp = [i for i in field(goods, 'price-color', 'non-existent-field')]
        self.assertEqual(len(resp), 0)

    def test_multi_args_random_empty(self):
        goods = [
            {'title': 'Ковер', 'color': 'green'},
            {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
            {'price': 300},
        ]
        resp = [i for i in field(goods, 'price', 'color')]
        self.assertEqual(len(resp), 3)
        for item in resp:
            if 'price' in item and 'color' in item:
                self.assertEqual(len(item), 2)
            elif 'price' in item:
                self.assertEqual(len(item), 1)
            elif 'color' in item:
                self.assertEqual(len(item), 1)


class TestRandom(TestCase):

    def test_type(self):
        r = gen_random(1, 10, 10)
        self.assertTrue(isinstance(r, GeneratorType))
        with self.assertRaises(TypeError):
            len(r)

    def test_len(self):
        length = 15
        r = [i for i in gen_random(1, 10, length)]
        self.assertEqual(len(r), length)

    def test_process(self):
        length = 10
        r = [i for i in gen_random(1, 1, length)]
        self.assertEqual(len(r), length)
        for item in r:
            self.assertEqual(item, 1)

    def test_range(self):
        length = 100
        _min, _max = 1, 8
        r = [i for i in gen_random(_min, _max, length)]
        self.assertEqual(len(r), length)
        for item in r:
            self.assertGreaterEqual(item, _min)
            self.assertLessEqual(item, _max)


class TestUniqueIterator(TestCase):

    def test_simple_range(self):
        data = range(10)
        r = [i for i in Unique(data)]
        data = [i for i in data]
        self.assertEqual(len(r), len(data))
        self.assertEqual(r, data)

    def test_simple_list(self):
        data = [i for i in range(11)]
        r = [i for i in Unique(data)]
        self.assertEqual(len(r), len(data))
        self.assertEqual(r, data)

    def test_simple_generator(self):
        data = (i for i in range(11))
        r = [i for i in Unique(data)]
        data = [i for i in range(11)]
        self.assertEqual(len(r), len(data))
        self.assertEqual(r, data)

    def test_simple_range_case(self):
        data = range(10)
        r = [i for i in Unique(data, ignore_case=True)]
        data = [i for i in data]
        self.assertEqual(len(r), len(data))
        self.assertEqual(r, data)

    def test_simple_list_case(self):
        data = [i for i in range(11)]
        r = [i for i in Unique(data, ignore_case=True)]
        self.assertEqual(len(r), len(data))
        self.assertEqual(r, data)

    def test_simple_generator_case(self):
        data = (i for i in range(11))
        r = [i for i in Unique(data, ignore_case=True)]
        data = [i for i in range(11)]
        self.assertEqual(len(r), len(data))
        self.assertEqual(r, data)

    def test_str(self):
        data = ['Abc', 'aBc', 'abC', 'abc']
        r = [i for i in Unique(data)]
        self.assertEqual(len(r), len(data))
        self.assertEqual(r, data)

    def test_str_case(self):
        data = ['Abc', 'aBc', 'abC', 'abc']
        res = ['Abc']
        r = [i for i in Unique(data, ignore_case=True)]
        self.assertEqual(len(r), len(res))
        self.assertEqual(r, res)

        data = ['aBc', 'Abc', 'abC', 'abc']
        res = ['aBc']
        r = [i for i in Unique(data, ignore_case=True)]
        self.assertEqual(len(r), len(res))
        self.assertEqual(r, res)

    def test_mix_case(self):
        data = ['aBc', 'Abc', 'abC', 'abc', 'dd', 1, 'abc']
        res = ['aBc', 'dd', 1]
        r = [i for i in Unique(data, ignore_case=True)]
        self.assertEqual(len(r), len(res))
        self.assertEqual(r, res)

    def test_with_random(self):
        _min, _max = 2, 7
        data = gen_random(_min, _max, 999)
        r = [i for i in Unique(data, ignore_case=True)]
        self.assertTrue(len(r) > 0)
        self.assertTrue(len(r) <= _max - _min + 1)
