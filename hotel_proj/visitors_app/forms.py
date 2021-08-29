from django import forms
from django.forms import ModelForm, Textarea
from .models import *
from django.core.exceptions import ValidationError

class SearchBookingForm(ModelForm):
    class Meta:
        model= Booking
        exclude = ('user', 'room')

    def clean_check_out_date(self):
        data = self.cleaned_data['check_in_date']
        check_out_date = self.cleaned_data['check_out_date']
        if data >= check_out_date:
            raise forms.ValidationError('check in must be after checkout')
        return check_out_date

class ContactForm(ModelForm):
    class Meta:
        model = Info
        fields = "__all__"

        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }