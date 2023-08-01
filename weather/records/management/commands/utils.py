from datetime import datetime
from typing import Union, List, Dict
import requests
from dotenv import load_dotenv
from locations.models import City


load_dotenv()


class CityResponse:
    """
    Класс для репрезентации ответа с эндпоинта
    'https://api.openweathermap.org/data/2.5/weather'.
    Экземпляр включает в себя только необходимую информацию.
    ----------
    Атрибуты:
        data : dict
            словарь с ответом с эндпоинта
    ----------
    """

    def __init__(self, data: Dict):
        """
        Создать атрибуты класса в соответствии с ответом с эндпоинта.
        """
        self.name = data['name']
        self.longitude = data['coord']['lon']
        self.latitude = data['coord']['lat']
        self.weather_id = data['weather'][0]['id']
        self.weather_main = data['weather'][0]['main']
        self.weather_description = data['weather'][0]['description']
        self.weather_icon = data['weather'][0]['icon']
        self.main_temp = data['main']['temp']
        self.main_feels_like = data['main']['feels_like']
        self.main_temp_min = data['main']['temp_min']
        self.main_temp_max = data['main']['temp_max']
        self.main_pressure = data['main']['pressure']
        self.main_humidity = data['main']['humidity']
        self.visibility = data['visibility']
        self.wind_speed = data['wind']['speed']
        self.wind_deg = data['wind']['deg']
        self.clouds_all = data['clouds']['all']
        self.dt = data['dt']

    @staticmethod
    def epoch_to_datetime(timestamp: Union[float, int]) -> datetime:
        """
        Cтатичный метод для конвертации эпохального
        времени в объект datetime.
        """
        return datetime.fromtimestamp(timestamp)

    def __str__(self):
        return (
            f"{self.name} || "
            f"{self.epoch_to_datetime(self.dt)} || "
            f"{self.main_temp}C"
        )


class RecordResponse:
    """
    Класс для репрезентации ответа с эндпоинта
    'https://api.openweathermap.org/data/2.5/forecast'.
    Экземпляр включает в себя только необходимую информацию.
    ----------
    Атрибуты:
        data : dict
            словарь с ответом с эндпоинта
    ----------
    """
    def __init__(self, data: Dict):
        """
        Создать атрибуты класса в соответствии с ответом с эндпоинта.
        """
        self.dt = data['dt']
        self.main_temp = data['main']['temp']
        self.main_feels_like = data['main']['feels_like']
        self.main_temp_min = data['main']['temp_min']
        self.main_temp_max = data['main']['temp_max']
        self.main_pressure = data['main']['pressure']
        self.main_humidity = data['main']['humidity']
        self.main_sea_level = data['main']['sea_level']
        self.main_grnd_level = data['main']['grnd_level']
        self.weather_id = data['weather'][0]['id']
        self.weather_main = data['weather'][0]['main']
        self.weather_description = data['weather'][0]['description']
        self.weather_icon = data['weather'][0]['icon']
        self.wind_speed = data['wind']['speed']
        self.wind_deg = data['wind']['deg']
        self.wind_gust = data['wind']['gust']
        self.clouds_all = data['clouds']['all']
        self.visibility = data['visibility']

    @staticmethod
    def epoch_to_datetime(timestamp: Union[float, int]) -> datetime:
        """
        Cтатичный метод для конвертации эпохального
        времени в объект datetime.
        """
        return datetime.fromtimestamp(timestamp)


class WeathermapApi:
    """
    Интерфейс для работы с openweather.org.
    """
    CITIES_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
    WEATHER_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
    COMMON_PARAMS = {
        'lang': 'ru',
        'units': 'metric',
    }

    def __init__(self, api_key):
        self.__api_key = api_key

        if not isinstance(api_key, str):
            raise TypeError(
                "Апи ключ должен быть типа \"str\". "
                f"В класс был передан {type(self.__api_key)}")

    def get_city(self, city: str) -> 'CityResponse':
        """
        Функция для получения географических координат города
        по названию. Возвращает экземпляр класса СityResponse.
        ----------
        Атрибуты:
            city : str
                Название города на русском языке.
        """
        params = dict(
            appid=self.__api_key,
            q=city,
            **self.COMMON_PARAMS,
        )
        response = requests.get(self.CITIES_ENDPOINT, params=params)
        if response.status_code == 200:
            return CityResponse(response.json())

    def get_records(
            self,
            city: City
    ) -> List['RecordResponse']:
        """
        Функция для получения прогноза погоды на четыре дня
        с диапазоном в три часа. Возвращает список экземпляров класса
        RecordResponse.
        ----------
        Атрибуты:
            city : class City
                Экземпляр класса Сity (Django модель).
        """
        data = []
        params = dict(
            appid=self.__api_key,
            lat=city.latitude,
            lon=city.longitude,
            **self.COMMON_PARAMS,
        )
        response = requests.get(self.WEATHER_ENDPOINT, params=params)
        if response.status_code == 200:
            for record in response.json()['list']:
                data.append(RecordResponse(record))
        return data
