from django.shortcuts import render
from django.http import HttpResponse 
from . import forms

from app.forms import NewUserForm

# Create your views here.


def index(request):
    return render(request,'app/index.html')

def form_name_view(request):
    form = forms.User()  

    if request.method =='POST':
        form = forms.User(request.POST)

        if form.is_valid():
            form.save() 
            return index(request)
        else:
            print('Eroare, forma gresita')

    return render(request,'app/form_page.html',{'form':form})