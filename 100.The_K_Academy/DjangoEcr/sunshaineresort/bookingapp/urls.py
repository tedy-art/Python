
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view),
    path('booking/', booking_view),
    path('display/', display_view),
    path('update/<int:id>/', update_view),
    path('delete/<int:id>/', delete_view),
]
