from .views import *
from django.urls import path 


urlpatterns = [
path('',home, name='home'),
path('about/',about, name='about'),
path('login/',login_user, name='login'),
path('logout/',logout_user, name='logout'),
path('register/',register_user, name='register'),
path('product/<int:pk>/',product, name='product'),
path('category/<str:foo>/',category, name='category'),
path('category_summary/',category_summary, name='category_summary'),
path('update_user/',update_user, name='update_user'),
path('update_password/',update_password, name='update_password'),

]