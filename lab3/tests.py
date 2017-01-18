#!/usr/bin/env python3

from datetime import date
from unittest import TestCase

import mock

from lab3.baseclass import BaseClient
from lab3.methods import GetUID
from lab3.main import get_age
from lab3.main import calc_histogram


class BaseClientTest(TestCase):

    def test_bad_init(self):
        with self.assertRaises(AssertionError):
            BaseClient()

    def test_invalid_http_method(self):
        class InvalidMethod(BaseClient):
            http_method = "delete"
            vk_method = "users.get"
        with self.assertRaises(AssertionError):
            InvalidMethod()

    def test_no_vk_method(self):
        class InvalidMethod(BaseClient):
            http_method = "get"
        with self.assertRaises(AssertionError):
            InvalidMethod()

    def test_init_ok(self):
        class OK(BaseClient):
            http_method = "get"
            vk_method = "users.get"
        OK()


class MockResponse(object):
    """Мок ответа либы requests"""
    def __init__(self, json_data):
        self.json_data = json_data
        self.status_code = 200

    def json(self):
        return self.json_data


def mocked_requests_get(*args, **kwargs):
    json_data = kwargs.pop('json_data', {})

    def inner(*args, **kwargs):
        return MockResponse(json_data)

    return inner


class GetUIDTest(TestCase):

    @mock.patch('lab3.baseclass.request',
                side_effect=mocked_requests_get(json_data={
                    'response': [
                        {
                            'uid': 1,
                        },
                        {
                            'uid': 2,
                        },
                    ],
                }))
    def test_response_processing(self, resp):
        r = GetUID(username='xxx').execute()
        self.assertEqual(r, 1)

    @mock.patch('lab3.baseclass.request',
                side_effect=mocked_requests_get(json_data={
                    'response': [{
                        'name': '1111',
                    }]
                }))
    def test_invalid_resp(self, resp):
        with self.assertRaises(Exception):
            GetUID(username='xxx').execute()

    @mock.patch('lab3.baseclass.request', side_effect=mocked_requests_get(json_data={}))
    def test_empty_resp(self, resp):
        r = GetUID(username='xxx').execute()
        self.assertIsNone(r)


class AgeCalcTest(TestCase):

    @mock.patch('lab3.main.datetime')
    def test_get_age_ok(self, datetime):
        datetime.date.today.return_value = date(2016, 1, 1)
        date_str = '29.08.1995'
        res = 21
        self.assertEqual(get_age(date_str), res)

    @mock.patch('lab3.main.datetime')
    def test_get_age_null(self, datetime):
        datetime.date.today.return_value = date(2016, 1, 1)
        date_str = '29.08'
        self.assertIsNone(get_age(date_str))

    def test_get_age_invalid(self):
        _date = date(2000, 5, 20)
        self.assertIsNone(get_age(_date))
        _date = '1.1.1.1'
        self.assertIsNone(get_age(_date))
        _date = '1995'
        self.assertIsNone(get_age(_date))


class CalcHistogramTest(TestCase):

    @mock.patch('lab3.main.datetime')
    def test_simple(self, datetime):
        datetime.date.today.return_value = date(2016, 1, 1)
        data = {'response': [
            {'bdate': '10.10.2000'},
            {'bdate': '10.10.2000'},
            {'bdate': '10.10.2000'},
        ]}
        res = calc_histogram(data)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0][0], 16)
        self.assertEqual(res[0][1], 100)

    @mock.patch('lab3.main.datetime')
    def test_simple_w_formats(self, datetime):
        datetime.date.today.return_value = date(2016, 1, 1)
        data = {'response': [
            {'bdate': '10.10'},
            {'bdate': '10.10.2000'},
            {'bdate': '10.10'},
            {'bdate': '10.10.2000'},
            {'bdate': '10.10.2000'},
            {'bdate': '10.10'},
            {'bdate': '10.10.2000'},
        ]}
        res = calc_histogram(data)
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0][0], 16)
        self.assertEqual(res[0][1], 100)

    @mock.patch('lab3.main.datetime')
    def test_medium(self, datetime):
        datetime.date.today.return_value = date(2016, 1, 1)
        data = {'response': [
            {'bdate': '10.10'},
            {'bdate': '10.10.2000'},
            {'bdate': '10.10'},
            {'bdate': '10.10.1990'},
            {'bdate': '10.10.1990'},
            {'bdate': '10.10'},
            {'bdate': '10.10.2000'},
        ]}
        res = calc_histogram(data)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0][0], 16)
        self.assertEqual(res[0][1], 50)
        self.assertEqual(res[1][0], 26)
        self.assertEqual(res[1][1], 50)
