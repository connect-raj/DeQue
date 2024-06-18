from django.urls import path
from .views import *

urlpatterns = [
  path('login/', admin_login, name='admin_login'),
  path('dashboard/', admin_home, name='admin_home'),
  path('restaurants/', admin_restaurant_list, name="admin_restaurant_list"),
  path('add-restaurants/', add_rest, name="add_rest"),
  path('restaurants/Activate/<id>/', Activate, name="Activate"),
  path('restaurants/close/<id>/', close_rest, name="close_rest"),
  path('restaurants/open/<id>/', open_rest, name="open_rest"),
  path('restaurants/Update/<id>/', Update, name="Update"),
  path('logout/', admin_logout, name="admin_logout")
]