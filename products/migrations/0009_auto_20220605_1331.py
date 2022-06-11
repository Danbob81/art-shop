# Generated by Django 3.2.13 on 2022-06-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220603_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='stock_qty',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.subcategory'),
        ),
    ]