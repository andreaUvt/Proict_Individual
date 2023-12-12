from django.db import models
from django.contrib.auth.models import User, AbstractUser,Group,Permission
from django.utils import timezone

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_favorite = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='foods')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    foods = models.ManyToManyField(Food)
    
    meal_choices = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('snack', 'Snack'),
        ('dinner', 'Dinner'),
        ('other', 'Other'),
    ]
    meal = models.CharField(max_length=10, choices=meal_choices)

    def __str__(self):
        return f"{self.user.username} - {self.name}"


class FavoriteFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} - {self.food.name}"
    
class CustomUser(AbstractUser):
    reset_token = models.CharField(max_length=255, blank=True, null=True)
    
    # Adaugă related_name pentru a evita conflictele
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='customuser_set')