# Generated by Django 5.1.3 on 2024-11-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0017_remove_engine_milage_car_milage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.IntegerField(verbose_name='Пробег'),
        ),
    ]
