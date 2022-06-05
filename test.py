import json
import unittest
from unittest.mock import MagicMock, patch

import main_weather_module as mwm


class Test_main_weather_module(unittest.TestCase):
    def test_weather_data(self):
        """ Выдает ли функция weather_data -> dict """
        self.assertEqual(type(mwm.weather_data(query='London')), dict)

    @patch('main_weather_module.req')
    def test_success_from_server(self, requests_mock):
        """ Проверка на то, что запрос работает верно (200) """
        with open('json_main_weather_module.json', 'r') as f:
            body = json.load(f)
        request_response_mock = MagicMock()
        request_response_mock.postcode = 200
        request_response_mock.json.return_value = body
        requests_mock.get.return_value = request_response_mock

    @patch('main_weather_module.req')
    def test_error_from_server(self, requests_mock):
        """ Проверка на то, что запрос выдает ошибку - 'city not found' (404) """
        request_response_mock = MagicMock()
        request_response_mock.postcode = 404
        request_response_mock.json.return_value = {'message': 'city not found'}
        requests_mock.get.return_value = request_response_mock


if __name__ == '__main__':
    unittest.main()
