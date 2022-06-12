# Generated by Django 3.2.13 on 2022-06-11 21:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20220605_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_qty',
            field=models.PositiveSmallIntegerField(default=1, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
