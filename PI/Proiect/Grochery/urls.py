from django.urls import path
from Grochery import views

app_name = 'Grochery'
main_page_name = 'main_page'

urlpatterns=[
    path('inregistrare/', views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('food_list/',views.food_list,name='food_list'),
    path('add_food/',views.add_food,name='add_food'),
    path('edit_food/<int:food_id>/',views.edit_food, name='edit_food'),
    path('delete_food/<int:food_id>/',views.delete_food,name='delete_food'),
    path('main_page/',views.main_page, name='main_page'),
    path('shopping_lists/', views.shopping_lists, name='shopping_lists'),
    path('reset_password/',views.reset_password,name='reset_password'),
    
]