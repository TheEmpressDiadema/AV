# Generated by Django 5.1.3 on 2024-11-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0004_alter_brand_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=20),
        ),
    ]