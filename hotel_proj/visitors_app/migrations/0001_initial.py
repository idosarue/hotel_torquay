# Generated by Django 3.2.6 on 2021-08-25 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_people', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_night', models.IntegerField(default=500)),
                ('room_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors_app.roomsize')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors_app.roomtype')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('stay_len', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visitors_app.room')),
            ],
        ),
    ]
