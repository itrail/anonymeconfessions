# Generated by Django 2.0 on 2018-04-06 20:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('anonyme_confessions', '0002_auto_20180406_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 6, 20, 31, 23, 907613, tzinfo=utc), verbose_name='Data opublikowania'),
        ),
    ]
