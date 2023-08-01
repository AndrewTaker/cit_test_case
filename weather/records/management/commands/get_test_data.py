import os
from typing import Any, List
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from locations.models import City
from records.models import Record
from records.management.commands.utils import WeathermapApi

load_dotenv()

WEATHERMAP_API_KEY: str = os.getenv('WEATHERMAP_API_KEY')
CITIES: List = [
    'Мурманск',
    'Апатиты',
    'Оленегорск',
    'Мончегорск',
    'Кандалакша',
    'Печенга',
    'Кировск',
    'Ковдор',
    'Ревда',
    'Ловозеро',
    'Кола',
    'Полярный',
    'Полярные Зори',
    'Североморск',
    'Снежногорск',
]


class Command(BaseCommand):
    CITIES_BULK: List = []
    RECORDS_BULK: List = []

    def handle(self, *args: Any, **options: Any):
        api = WeathermapApi(WEATHERMAP_API_KEY)

        for city in CITIES:
            city_data = api.get_city(city)
            if city_data:
                model_instance = City(
                    name=city_data.name,
                    latitude=city_data.latitude,
                    longitude=city_data.longitude
                )
                if not City.objects.filter(
                    name=model_instance.name,
                    latitude=model_instance.latitude,
                    longitude=model_instance.longitude,
                ).exists():
                    self.CITIES_BULK.append(model_instance)
                    self.stdout.write(self.style.SUCCESS(
                            f"Город {model_instance.name} записан в базу."
                        )
                    )
                else:
                    self.stdout.write(self.style.NOTICE(
                            f"Город {model_instance} уже существует в базе."
                        )
                    )
        City.objects.bulk_create(self.CITIES_BULK)
        self.stdout.write(self.style.SUCCESS(
                f"{len(self.CITIES_BULK)} городов внесены в базу."
            )
        )

        cities = City.objects.all()
        for city in cities:
            records = api.get_records(city)
            for record in records:
                if record:
                    record_instance = Record(
                        city=city,
                        datetime=record.epoch_to_datetime(record.dt),
                        c_value=record.main_temp
                    )
                    if not Record.objects.filter(
                        city=record_instance.city,
                        datetime=record_instance.datetime,
                    ).exists():
                        self.RECORDS_BULK.append(record_instance)
            self.stdout.write(self.style.SUCCESS(
                    f"Получены записи для {city.name}"
                )
            )
        Record.objects.bulk_create(self.RECORDS_BULK)
        self.stdout.write(self.style.SUCCESS(
                f"{len(self.RECORDS_BULK)} записей внесены в базу."
            )
        )
