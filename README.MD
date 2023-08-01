# Монолитное приложение для мониторинга погоды.
### Стэк
- Django 4.2.3
- Jquery 3.7.0
- Chart.js 4.0
### Локальный запуск
`https://github.com/AndrewTaker/cit_test_case.git` загрузить без ssh
`git@github.com:AndrewTaker/cit_test_case.git` заугрузить, используя ssh

`pip install -r requirements.txt` установить зависимости
`python manage.py makemigrations` создать миграции
`python manage.py migrate` установить миграции
### Вариант запуска с живыми данными
`python manage.py get_test data` позволяет получить прогноз на ближайшие четыре дня с диапазоном в три часа. Чтобы воспользоваться этой функцией, нужно создать в корне проекта _в той же папке, где файл `requirements.txt`_ файл .env и наполнить его следующими данными:
```
DJANGO_SECRET_KEY = "django-insecure-c9_hbav=odxxbiq=k556i5x4+s#4(l!-)i#-hmd=_hc(^dp)63"
WEATHERMAP_API_KEY = "352af66624e63bf7bd6f93785a164b4d"
```
