# Generated by Django 2.2.5 on 2019-09-10 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190910_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 9, 10, 12, 18, 28, 9637), null=True, verbose_name='Дата выполнения'),
        ),
    ]
