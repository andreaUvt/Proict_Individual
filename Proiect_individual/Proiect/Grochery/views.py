from django.shortcuts import render
#from Grochery.models import User
from Grochery.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'Grochery/index.html')

def register(request):
    
    form = NewUserForm

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Eroare,forma gresita')
    return render(request,'Grochery/users.html',{'form':form})