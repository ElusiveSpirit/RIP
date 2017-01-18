#!/usr/bin/env python3

import os

from requests.api import request


class VKAPIError(Exception):

    def __init__(self, status_code, data):
        self.status_code = status_code
        self.raw_data = data
        self.vk_code = data.get('code')
        self.message = data.get('message')


class BaseClient:
    BASE_URL = "https://api.vk.com/method/"
    vk_method = None
    http_method = None

    headers = None
    params = None
    json = None

    def __init__(self):
        assert isinstance(self.http_method, str) and self.http_method.lower() in ('get', 'post'), \
            "В BaseClient доступны только GET и POST методы"
        assert isinstance(self.http_method, str) and isinstance(self.vk_method, str), \
            "http_method и vk_method должны быть определены"

    def generate_url(self):
        """Склейка url"""
        return os.path.join(self.BASE_URL, self.vk_method)

    def _get_data(self):
        """Отправка запроса к VK API"""
        r = request(
            method=self.http_method,
            url=self.generate_url(),
            headers=self.headers,
            params=self.params,
            json=self.json,
            timeout=(3, 30),
        )
        return self.response_handler(r)

    def response_handler(self, response):
        """Обработка ответа от VK API"""
        try:
            data = response.json()
            if 200 <= response.status_code < 300:
                return data
            raise VKAPIError(
                status_code=response.status_code,
                data=data,
            )
        except:
            print(response.text)
            print(response.request.method)
            print(response.request.url)
            return {}

    def execute(self):
        """Запуск клиента"""
        return self._get_data()
