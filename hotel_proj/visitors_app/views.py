from django.forms.utils import pretty_name
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404 ,HttpResponse
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
    

class CreateBooking(generic.CreateView):
    template_name = 'visitors/room_list.html'
    form_class = SearchBookingForm

    def find_booking(self): # new
        form = SearchBookingForm(self.request.GET)
        if form.is_valid():
            people_num = form.cleaned_data['number_of_people']
            start_date = form.cleaned_data['check_in_date']
            end_date = form.cleaned_data['check_out_date']
            rooms = Room.objects.all()

            room_li = []
            for room in rooms:
                if room.is_vacant(start_date, end_date):
                    if room.room_type_id == people_num.max_people:
                        return {'room':room, 'end_date':end_date, 'start_date':start_date, 'people_num':people_num,'room_id':room.id}
            else:
                raise forms.ValidationError('no rooms available')
                
        else:
            return redirect('search_booking')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.find_booking()
        return context

        
    def post(self, request, *args, **kwargs):
        form = self.request.POST
        people = RoomSize.objects.get(max_people=form['id'])
        Booking.objects.create(check_in_date=self.find_booking()['start_date'], check_out_date=self.find_booking()['end_date'], number_of_people=people, room=Room.objects.get(id=form['id']),user=request.user.profile)
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = SearchBookingForm(request.GET)
        if not form.is_valid():
            messages.error(request, 'check in must be after checkout.')
            return redirect('search_booking')
        return super().get(request, *args, **kwargs)


class CreateContact(generic.CreateView):
    form_class = ContactForm
    template_name = 'visitors/contact.html'


    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'contact form submitted')
            Info.objects.create(**form.cleaned_data)
            return redirect('info')
        return super().post(request, *args, **kwargs)
    
# class Info(models.Model):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#     content = models.CharField(max_length=255)

# class Review(models.Model):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#     content = models.CharField(max_length=255)
#     class Rating(models.IntegerChoices):
#         GREAT = 1
#         AMAZING = 2
#         AWESOME = 3
#     rating = models.IntegerField(choices=Rating.choices)

class CreateReview(generic.CreateView):
    form_class = ReviewForm
    template_name = 'visitors/review.html'


    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Review form submitted')
            Review.objects.create(**form.cleaned_data)
            return redirect('info')
        return super().post(request, *args, **kwargs)




