from django.shortcuts import render
from Grochery.forms import UserForm 

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Food, ShoppingList,FavoriteFood
from .forms import FoodForm,ShoppingListForm
from django.shortcuts import redirect,get_object_or_404
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'Grochery/index.html')

@login_required
def special(request):
    return HttpResponse("You are loged in")

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else: 
        user_form = UserForm()

    return render(request,'Grochery/inregistrare.html',{'user_form':user_form,'registered':registered})
         
    
def user_login(request):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user) 
                return redirect(reverse('main_page'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tryed to log in and failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("invalid login details")
    else:
        return render(request,'Grochery/log_in.html')
    


    
@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user  # Set the user to the currently logged-in user
            food.is_favorite = form.cleaned_data['is_favorite']
            food.save()
            return redirect('Grochery:food_list')
        else:
            print(form.errors)
    else:
        form = FoodForm()
    return render(request, 'Grochery/add_food.html', {'form': form})




@login_required
def food_list(request):
    sort_option = request.GET.get('sort', 'name')

    if sort_option == 'name':
        foods = Food.objects.filter(user=request.user).order_by('name')
    elif sort_option == '-name':
        foods = Food.objects.filter(user=request.user).order_by('-name')
    elif sort_option == 'is_favorite':
        foods = Food.objects.filter(user=request.user).order_by('-is_favorite', 'name')
    else:
        foods = Food.objects.filter(user=request.user)

    return render(request, 'Grochery/food_list.html', {'foods': foods})

def edit_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)

    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.is_favorite = form.cleaned_data['is_favorite']
            food.save()
            return redirect('Grochery:food_list')

    form = FoodForm(instance=food)
    return render(request, 'Grochery/edit_food.html', {'form': form})

def delete_food(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    food.delete()
    return HttpResponseRedirect(reverse('Grochery:food_list'))

@login_required
def main_page(request):
    return render(request, 'Grochery/main.html')

@login_required
def shopping_lists(request):
    user_lists = ShoppingList.objects.filter(user=request.user)
    return render(request, 'Grochery/shopping_lists.html', {'user_lists': user_lists})

@login_required
def add_shopping_list(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            shopping_list = form.save(commit=False)
            shopping_list.user = request.user
            shopping_list.save()
            return redirect('Grochery:shopping_lists')
    else:
        form = ShoppingListForm()
    return render(request, 'Grochery/add_shopping_list.html', {'form': form})