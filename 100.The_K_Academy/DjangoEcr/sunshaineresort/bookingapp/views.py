from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request,'bookingapp/homepage.html')

def booking_view(request):
    print(request.method)

    return render(request, 'bookingapp/bookingpage.html')