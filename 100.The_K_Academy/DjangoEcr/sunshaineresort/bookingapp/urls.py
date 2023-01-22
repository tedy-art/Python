
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view, name ='index'),
    path('booking/', booking_view, name='booking'),
]
