# Generated by Django 2.2.5 on 2019-09-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20190910_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения'),
        ),
    ]
