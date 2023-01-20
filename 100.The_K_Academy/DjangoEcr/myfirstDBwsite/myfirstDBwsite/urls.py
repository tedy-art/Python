
from django.contrib import admin
from django.urls import path
from myfirstapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index_view),
    path('display/', display_view),
    path('update/<int:id>/', update_view),
]
