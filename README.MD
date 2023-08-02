# Монолитное приложение для мониторинга погоды.
### Стэк
- Django 4.2.3
- Jquery 3.7.0
- Chart.js 4.0
### Локальный запуск
`git clone https://github.com/AndrewTaker/cit_test_case.git` загрузить без ssh

`git clone git@github.com:AndrewTaker/cit_test_case.git` загрузить, используя ssh

`python -m venv venv` создать стандартное виртуальное окружение

`source venv/bin/activate` активировать окружение для POSIX

`source venv/scripts/activate` активировать окружение для Windows

`pip install -r requirements.txt` установить зависимости

`python manage.py makemigrations` создать миграции

`python manage.py migrate` применить миграции

### Вариант запуска с живыми данными
`python manage.py get_test_data` позволяет получить прогноз на ближайшие четыре дня с диапазоном в три часа. Чтобы воспользоваться этой функцией, нужно создать в корне проекта _в той же директории, где файл `requirements.txt`_ файл `.env` и наполнить его следующими данными:
```
DJANGO_SECRET_KEY = Django `SECRET_KEY` из файла setting.py
WEATHERMAP_API_KEY = API ключ для сервиса  Open Weather Map https://openweathermap.org/
```
### Вариант с дампом
В директории с файлом `manage.py` лежит файл `database.json`, в котором уже есть предзаполненные данные.
Для заполнения базы нужно использовать команду `python manage.py loaddata database.json`
### Тестовый пользователь
`python manage.py create_test_user` команда создает тестового пользователя с случайно сгенерированным паролем. Пароль и имя пользователя будут выведены в консоль. Пароль захеширован и является полноценным.
