from django.urls import path
from Grochery import views

#lista pentru site urile legate in afara de cea principala
app_name= 'Grochery_sites'

urlpatterns = [ 
    path('',views.register,name='register'),
]