# Generated by Django 5.1.3 on 2024-11-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0007_alter_carmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='gen',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=60),
        ),
    ]
