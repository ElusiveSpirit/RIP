# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2


def print_result(f):

    def inner(*args, **kwargs):
        print(f.__name__)
        res = f(*args, **kwargs)
        if isinstance(res, (str, int)):
            print(res)
        elif isinstance(res, dict):
            print('\n'.join("{}={}".format(k, v) for k, v in res.items()))
        elif hasattr(res, '__iter__'):
            print('\n'.join([str(i) for i in res]))
        else:
            raise NotImplementedError('type {} unsupported ({})'.format(type(res), res))
        return res

    return inner
