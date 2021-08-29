from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(RoomSize)
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Booking)
admin.site.register(Info)
admin.site.register(Review)