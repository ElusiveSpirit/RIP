#!/usr/bin/env python3

class Unique(object):
    """Итератор для удаления дубликатов"""

    def __init__(self, items, **kwargs):
        self.items = [i for i in items]
        self.ignore_case = kwargs.pop('ignore_case', False)
        self.unique = []
        self.append = self.unique.append

    def __iter__(self):
        return self

    def __next__(self):
        try:
            while True:
                item = self.items.pop(0)
                _item = item
                if self.ignore_case and isinstance(item, str):
                    _item = item.lower()
                if _item not in self.unique:
                    # сохраняем в ловеркейсе (если ignore_case), отдаём оригинал всегда
                    self.append(_item)
                    return item
        except IndexError:
            raise StopIteration
