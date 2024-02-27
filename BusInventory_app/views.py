from django.shortcuts import render, HttpResponseRedirect, reverse,redirect
from . import forms, models
from .models import Bus
from .forms import BusForm
from django.urls import reverse


def bus_list_view(request):
    buses = Bus.objects.all()
    return render(request, 'bus_list.html', {'buses': buses})

def home(request):
    return render(request, 'home.html')



def add_bus_view(request):
    busForm=forms.BusForm()
    if request.method=="POST":
        busForm=forms.BusForm(request.POST,request.FILES)
        if busForm.is_valid():
            busForm.save()
        return HttpResponseRedirect('/bus-list/')
    return render(request,'add_bus.html',{'busForm':busForm})    



def delete_bus_list_view(request,pk):
    bus=models.Bus.objects.get(id=pk)
    bus.delete()
    return redirect('bus_list')


def update_bus_list_view(request,pk):
    bus=models.Bus.objects.get(id=pk)
    busForm=forms.BusForm(instance=bus)
    if request.method=='POST':
        busForm=forms.BusForm(request.POST,request.FILES,instance=bus)
        if busForm.is_valid():
            busForm.save()
            return redirect('bus_list')
    return render(request,'update_bus_list.html',{'busForm':busForm})


