"""
1. создать функцию(ии) для определения погоды по данным(Город). def weather_data(query), def weather_info(postcode):
2. Вынести некоторые данные в константу(ы). BASE_URL, API_KEY
3. Для запуска функции использовать if __name__ == '__main__': запуск! есть
4. Создать файл test.py внутри создать Класс для тестирования функции, с помощью unittest. - использовал mock
"""

import datetime as dt
import json

import requests as req


def weather_data(query) -> dict:
    API_KEY: str = '74822f51f7ec343352d180bf5c722ebd'
    BASE_URL: str = 'http://api.openweathermap.org/data/2.5/weather?'
    complete_query = BASE_URL + 'appid=' + API_KEY + '&q=' + query
    response: dict = req.get(complete_query).json()
    return response


def weather_info(postcode) -> dict:
    if postcode["cod"] != "404":
        temp_kelvin_info: float = postcode['main']['temp']
        temp_celsius_info: float = temp_kelvin_info - 273.15
        feels_like_kelvin_info: float = postcode['main']['feels_like']
        feels_like_celsius_info: float = feels_like_kelvin_info - 273.15
        wind_speed_info: float = postcode['wind']['speed']
        humidity_info: int = postcode['main']['humidity']
        description_info: str = postcode['weather'][0]['description']
        sunrise_time_info = dt.datetime.utcfromtimestamp(postcode['sys']['sunrise'] + postcode['timezone'])
        sunset_time_info = dt.datetime.utcfromtimestamp(postcode['sys']['sunset'] + postcode['timezone'])
        print(f"Temperature in {city}: {temp_celsius_info:.2f}°C")
        print(f"Temperature in {city} feels like: {feels_like_celsius_info:.2f}°C")
        print(f"Wind speed in {city}: {wind_speed_info}m/s")
        print(f"Humidity in {city}: {humidity_info}%")
        print(f"General weather in {city}: {description_info}")
        print(f"Sun rises in {city} at {sunrise_time_info} local time")
        print(f"Sun sets in {city} at {sunset_time_info} local time")
    else:
        print('city not found'.title())
    return postcode


if __name__ == '__main__':
    city: str = input('Select the city where you would like to know the weather:\n')
    weather_request: dict = weather_data(city)
    weather_data: dict = weather_info(weather_request)

# with open('json_main_weather_module.json', 'w') as f:
#     json.dump(weather_data, f, indent=2) # using fo mock, to create a json file.
