# Generated by Django 2.2.5 on 2019-09-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20190906_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(blank=True, max_length=300, verbose_name='Название'),
        ),
    ]
