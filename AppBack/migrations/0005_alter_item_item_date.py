# Generated by Django 3.2.8 on 2022-12-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBack', '0004_item_item_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_date',
            field=models.DateField(),
        ),
    ]
