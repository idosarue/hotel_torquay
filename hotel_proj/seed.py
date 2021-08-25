import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel_proj.settings')
django.setup()
from visitors_app.models import *

def create_room_type():
    type_li = ['Single', 'Double', 'Triple', 'Quad']
    for room in type_li:
        RoomType.objects.create(name=room)

# create_room_type()

def create_room_size():
    size_li = list(range(1,5))
    for size in size_li:
        RoomSize.objects.create(max_people=size)
# create_room_size()


def create_room(num):
    type_li = RoomType.objects.all()
    size_li = RoomSize.objects.all()
    price_li = [700, 1000, 1300, 1600]
    for _ in range(num):
        for x in range(4):
            Room.objects.create(room_size=size_li[x], room_type=type_li[x], price_per_night=price_li[x])

create_room(10)