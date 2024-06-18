from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contactus/', views.contactus,name='contactus'),
    path('index/', views.index,name='index')
    
]
