from typing import Any
from random import choice, randint
from string import ascii_uppercase, ascii_lowercase, digits
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


def generate_password(
        size: int = 8,
        chars: str = ascii_uppercase + digits + ascii_lowercase
) -> str:
    """
    Функция для генерации случайного пароля.
    По стандарту возвращает пароль, состоящий
    из восьми символов (цифры + буквы) разных регистров.
    """
    password = ''.join(choice(chars) for _ in range(size))
    for digit in digits:
        if digit in password:
            return password
        else:
            random_number = randint(0, 9)
            random_index = randint(0, size-1)
            password.replace(password[random_index], str(random_number))


USERNAME = 'test_user'
PASSWORD = generate_password()
EMAIL = f"{USERNAME}@test.com"


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        user = User.objects.create_user(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        if User.objects.filter(
            username=user.username,
            email=user.email
        ).exists():
            self.stdout.write(self.style.SUCCESS(
                    "Cоздан тестовый пользователь:\n"
                    f"username: {USERNAME}" + '\n'
                    f"password: {PASSWORD}" + '\n'
                    "Только для тестирования!"
                )
            )
        else:
            self.stdout.write(self.style.ERROR('SOMETHING WENT WRONG'))
