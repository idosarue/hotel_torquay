from django.shortcuts import redirect, render, get_list_or_404
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
        form = SearchBookingForm(self.request.GET)
        if form.is_valid():
            people_num = form.cleaned_data['number_of_people'].max_people
            # room_num = form.cleaned_data['number_of_rooms']
            start_date = form.cleaned_data['check_in_date']
            end_date = form.cleaned_data['check_out_date']
            rooms = Room.objects.all()
            room_li = []
            room = Room.objects.get(id=people_num)
            if room.is_vacant(start_date, end_date):
                print(room)
                return room
            # if people_num == room_num:
            #     for _ in range(room_num):
            #         print(people_num)
            #         room_li.append(Room.objects.get(id=1))
            # elif people_num > room_num:
            #     mod = int(people_num) % room_num
            #     if mod:
            #         x = mod
            #         for _ in range(room_num-1):
            #             room_li.append(Room.objects.get(id=x))
            #         room_li.append(Room.objects.get(id=x+1)) 
            #     else:
            #         for _ in range(room_num):
            #             x = people_num/room_num
            #             room_li.append(Room.objects.get(id=x))
            # else:
            #     room_li.append(Room.objects.get(id=1))
            # for room in rooms:
            #     if room.is_vacant(start_date, end_date):
            #         print(room_li)
            #         return room_li


        else:
            print('error')



def get_booking(request, pk):
    f = Room.objects.filter(id=pk)  
    Booking.objects.create()
    return redirect('info') 


