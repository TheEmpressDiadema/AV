# Generated by Django 5.1.3 on 2024-11-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0006_alter_carmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='slug',
            field=models.SlugField(max_length=30, unique=True),
        ),
    ]