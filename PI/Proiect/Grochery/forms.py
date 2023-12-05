from django import forms
from django.contrib.auth.models import User
from .models import Food,ShoppingList

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User 
        fields = ('username','email','password')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name','price','is_favorite']

class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['name', 'meal']