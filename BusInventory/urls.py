"""
URL configuration for BusInventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BusInventory_app import views
from BusInventory_app.views import bus_list_view, add_bus_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('bus-list/', bus_list_view, name='bus_list'),
    path('add-bus/', add_bus_view, name='add_bus'),
    path('delete-bus-list/<int:pk>',views.delete_bus_list_view, name='delete-bus-list'),
    path('update-bus-list/<int:pk>',views.update_bus_list_view,name='update-bus-list'),


]
