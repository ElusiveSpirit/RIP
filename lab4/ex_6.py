#!/usr/bin/env python3

import json
import sys

from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique


@print_result
def f1(arg):
    return list(unique(field(arg, 'job-name'), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda name: name.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda item: '{} с опытом Python'.format(item.strip()), arg))


@print_result
def f4(arg):
    money = gen_random(100000, 200000, len(arg))
    return ['{}, зарплата {} руб.'.format(i, j) for i, j in zip(arg, money)]


if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]

    with open(path) as f:
        data = json.load(f)

    with timer():
        f4(f3(f2(f1(data))))
