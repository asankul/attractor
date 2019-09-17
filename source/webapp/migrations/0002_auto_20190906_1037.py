# Generated by Django 2.2.5 on 2019-09-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(blank=True, default='new', max_length=200, verbose_name='Статус'),
        ),
    ]
