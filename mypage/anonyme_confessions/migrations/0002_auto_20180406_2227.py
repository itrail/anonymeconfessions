# Generated by Django 2.0 on 2018-04-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonyme_confessions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentator_nick',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
