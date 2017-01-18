#!/usr/bin/env python3

import random


def field(items, *args):
    """Генератор вычленения полей из массива словарей

        >>> goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
        >>>          {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
        >>> field(goods, 'title')
        'Ковер'
        'Диван для отдыха'
        >>> field(goods, 'title', 'price')
        {'title': 'Ковер', 'price': 2000}
        {'title': 'Диван для отдыха', 'price': 5300}
    """
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            res = item.get(args[0])
        else:
            res = {arg: item.get(arg) for arg in args if item.get(arg)}
        if res:
            yield res


def gen_random(begin, end, num_count):
    """Генератор списка случайных чисел
    >>> gen_random(1, 3, 5)
        [2, 2, 3, 2, 1]
    """
    return (random.randint(begin, end) for i in range(num_count))
