import types

def find_min(arr):
    assert isinstance(arr, (list, tuple, set, range, types.GeneratorType))
    return min(arr)


def find_average(arr):
    return sum(arr) / len(arr)
