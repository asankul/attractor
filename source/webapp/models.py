from django.db import models
import datetime

class Article(models.Model):
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
    title = models.CharField(max_length=300, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField(choices=status_choices, max_length=200, null=False, blank=False, default='new', verbose_name='Статус')
    date = models.DateField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)



