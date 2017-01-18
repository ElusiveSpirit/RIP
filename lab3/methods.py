#!/usr/bin/env python3

from lab3.baseclass import BaseClient


class GetUID(BaseClient):
    """Класс для получения id пользователя по короткому имени
    """
    vk_method = "users.get"
    http_method = "get"
    params = {
        'version': '5.59',
    }

    def __init__(self, username):
        self.params['user_ids'] = username
        super(GetUID, self).__init__()

    def execute(self):
        data = self._get_data()
        for item in data.get('response', []):
            user_id = item.get('uid')
            if not user_id:
                raise Exception("uid not found in {}".format(item))
            return user_id


class GetFriends(BaseClient):
    """Класс для получения диаграммы возрастов друзей человека по user_id
    """
    vk_method = "friends.get"
    http_method = "get"
    params = {
        'version': '5.59',
        'fields': 'bdate',
    }

    def __init__(self, user_id):
        self.params['user_id'] = int(user_id)
        super(GetFriends, self).__init__()
