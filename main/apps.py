from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Основное приложение' # работает только, если приложение в settings подключено правильно
