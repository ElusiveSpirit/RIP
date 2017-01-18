#!/usr/bin/env python3

from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
print('{}\n--\n{}'.format('\n'.join([str(i) for i in Unique(data1)]), '\n'.join([str(i) for i in Unique(data2)])))
