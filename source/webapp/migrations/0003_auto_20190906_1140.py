# Generated by Django 2.2.5 on 2019-09-06 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190906_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(blank=True, choices=[('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')], default='new', max_length=200, verbose_name='Статус'),
        ),
    ]
