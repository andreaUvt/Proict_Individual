from django.contrib import admin
from Grochery.models import UserProfileInfo,Food,ShoppingList,FavoriteFood
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(Food)
admin.site.register(ShoppingList)
admin.site.register(FavoriteFood)
