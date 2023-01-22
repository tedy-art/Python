from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index_view(request):
    return render(request,'bookingapp/homepage.html')

def booking_view(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
        uname = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        adhar = request.POST.get('adhar')
        date = request.POST.get('date')
        days = request.POST.get('days')
        status = request.POST.get('status')
        person = request.POST.get('persons')
        rtype = request.POST.get('rtype')

        booking = Bookings(Name=uname, email_id=email, mobile=mobile, days=days, adhar_no=adhar, status = status, no_of_persons = person, booking_date=date, room_type=rtype)
        booking.save()
        return redirect('/display/')

    return render(request, 'bookingapp/bookingpage.html')