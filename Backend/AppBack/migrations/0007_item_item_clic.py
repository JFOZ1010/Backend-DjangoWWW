# Generated by Django 3.2.8 on 2022-12-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBack', '0006_alter_history_item_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_clic',
            field=models.IntegerField(default=0),
        ),
    ]