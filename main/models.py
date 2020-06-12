from django.db import models


class Slider(models.Model):
    name = models.CharField(max_length=100,
                            help_text='просто название слайда до 100 символов, оно не отображается',
                            verbose_name='Название слайда')
    title = models.CharField(blank=True,
                             max_length=150,
                             help_text='до 150 символов, заполнять необязательно',
                             verbose_name='Заголовок на слайде')
    description = models.CharField(blank=True,
                                   max_length=150,
                                   help_text='до 150 символов, заполнять необязательно',
                                   verbose_name='Текст под заголовком')
    slideimg = models.ImageField(blank=False,
                                 upload_to='slider/',
                                 help_text='изображение обрежется, поэтому лучше брать большое',
                                 verbose_name='Добавить изображение')
    namebutton = models.CharField(blank=True,
                                  max_length=15,
                                  help_text='до 15 символов, необязательно',
                                  verbose_name='Название кнопки')
    linkbutton = models.URLField(blank=True,
                                 help_text='заполнить, если написали название кнопки',
                                 verbose_name='Ссылка на кнопку')

    class Meta:
        verbose_name = 'Блок 1.0: Слайдер'
        verbose_name_plural = 'Блок 1.0: Слайдеры'

    def __str__(self):
        return self.name


# Полезные моменты:
# - как только создал модель, то делаеш команду
# - python manage.py makemigrations - таким образом будет подготовлена миграция для базы данных
# - если ошибок не выскочило, то потом команда python manage.py migrate
# - это уже миграция в базу