from django import forms
from django.forms import ModelForm, fields
from .models import *

class SearchBookingForm(forms.ModelForm):
    class Meta:
        model= Booking
        exclude = ('room',)