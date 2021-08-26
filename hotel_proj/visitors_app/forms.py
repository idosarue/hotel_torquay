from django import forms
from django.forms import ModelForm, fields
from .models import *
from django.core.exceptions import ValidationError

class SearchBookingForm(forms.ModelForm):
    class Meta:
        model= Booking
        exclude = ('room',)
 