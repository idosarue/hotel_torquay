# Generated by Django 3.2.6 on 2021-08-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors_app', '0013_auto_20210828_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_out_date',
            field=models.DateField(),
        ),
    ]