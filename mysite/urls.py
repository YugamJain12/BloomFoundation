from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('events',views.events),
    path('about',views.about),
    path('contact',views.contact),
    path('donate',views.donate),
]