from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Bus  



class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_number', 'brand', 'number_of_seats', 'trip', 'trip_duration', 'conductor', 'driver']

