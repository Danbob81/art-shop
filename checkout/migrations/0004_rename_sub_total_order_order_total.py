# Generated by Django 3.2.13 on 2022-05-15 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220515_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='sub_total',
            new_name='order_total',
        ),
    ]
