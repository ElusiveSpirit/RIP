#!/usr/bin/env python3

import sys
import datetime
from collections import defaultdict

from lab3.methods import GetUID
from lab3.methods import GetFriends


def get_age(date):
    """Получить возраст из строки с датой рождения"""
    if isinstance(date, str):
        today = datetime.date.today()
        date = date.split('.')
        if len(date) == 3:
            return int(today.year) - int(date[2])
    return None


def calc_histogram(data):
    """Посчитать кол-во каждого возраста, нормализировать"""
    res = defaultdict(int)
    for item in data.get('response', []):
        age = get_age(item.get('bdate'))
        if age:
            res[age] += 1
    total = sum(res.values())
    _res = []
    append = _res.append
    for key, value in res.items():
        append((key, 100 * value / total))
    _res.sort(key=lambda item: item[0])
    return _res


if __name__ == "__main__":
    args = sys.argv[1:]
    assert len(args) > 0, "Ожидался int:user_id или str:username на вход программы"

    # спрашиваем uid у вк или используем тот, что получили
    try:
        user_id = int(args[0])
        print("Получен user_id={}\n".format(user_id))
    except (TypeError, ValueError):
        user_id = GetUID(username=args[0]).execute()
        print("Получен user_id={} из {}\n".format(user_id, args[0]))

    friends = GetFriends(user_id=user_id).execute()

    print("Распечатываем диаграмму друзей:\n")
    histogram = calc_histogram(friends)

    for (age, percent) in histogram:
        print("{}\t{}".format(age, '#' * int(percent)))
