from django.core.exceptions import ValidationError
from django.db import models
from accounts.models import Profile
from django.utils import timezone
# Create your models here.

class Booking(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    # number_of_rooms = models.IntegerField(default=1)
    number_of_people = models.ForeignKey('RoomSize', on_delete=models.PROTECT, null=True)
    room = models.ForeignKey('Room', on_delete=models.PROTECT)
    
    def is_vacant(self):
        if self.room.is_vacant:
            return True
        else:
            return False


class RoomType(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class RoomSize(models.Model):
    max_people = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.max_people}'

class Room(models.Model):
    room_size= models.ForeignKey(RoomSize, on_delete=models.PROTECT)
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    price_per_night = models.IntegerField(default=500)

    def __str__(self):
        return self.room_type.name
    
    def is_vacant(self, start_date, end_date):
        bookings = self.booking_set.exclude(check_out_date__lt=start_date, check_in_date__gt=end_date)
        if not bookings.exists():
            return True
        else:
            return False
        
