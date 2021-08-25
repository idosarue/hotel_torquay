from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def info(request):
    return render(request, 'visitors/info.html')

class SearchBooking(generic.FormView):
    form_class = SearchBookingForm
    template_name = 'visitors/search_booking.html'

class RoomList(generic.ListView):
    template_name = 'visitors/room_list.html'

    def get_queryset(self): # new
        people_num = int(self.request.GET.get('number_of_people'))
        room_num = int(self.request.GET.get('number_of_rooms'))
        if people_num == room_num:
            x = people_num/room_num
        else:
            x = people_num - room_num
        room_type = RoomType.objects.filter(id__lte=x)
        print(room_type)
        if Room.is_vacant:
            return room_type
