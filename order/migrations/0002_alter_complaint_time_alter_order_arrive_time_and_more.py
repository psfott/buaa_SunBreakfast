# Generated by Django 4.2.7 on 2023-12-03 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 16, 54, 26, 989143)),
        ),
        migrations.AlterField(
            model_name='order',
            name='arrive_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 16, 54, 26, 988141)),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='ride_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 3, 16, 54, 26, 988141)),
        ),
    ]
