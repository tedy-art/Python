from django.shortcuts import render
from myfirstapp.models import student

# Create your views here.
def index_view(request):
    return render(request, 'myfirstapp/index.html')

def display_view(request):
    data = student.objects.all()
    context = {'data':data}
    return render(request, 'myfirstapp/display.html', context)

def update_view(request, id):
    data = student.objects.get(pk = id)
    context = {'data' : data}
    return render(request, 'myfirstapp/update.html', context)