# Generated by Django 3.2.15 on 2022-10-12 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_auto_20221005_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 12, 13, 0, 20, 378179)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 13, 0, 20, 378179)),
        ),
    ]