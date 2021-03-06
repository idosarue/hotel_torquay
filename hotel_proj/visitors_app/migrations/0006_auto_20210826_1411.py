# Generated by Django 3.2.6 on 2021-08-26 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors_app', '0005_booking_number_of_rooms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_vacant',
        ),
        migrations.AlterField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors_app.room'),
        ),
    ]
