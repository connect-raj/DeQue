from django.urls import path
from .views import *

urlpatterns = [
  path('login/', user_login, name="login"),
  path('register/',signup,name="signup"),
  path('logout/',user_logout,name="logout"),
  path('order/',order,name="order"),
  path('restaurants/', user_restaurant, name="user_restaurant"),
  path('restaurants/<name>', restaurant_page, name="restaurant_page"),
  path('', user_home, name="user_home"),
  path('home/', user_home, name="user_home"),
  path('restaurants/<name>/tables/', layout_restaurant, name="layout_restaurant"),
  path('restaurants/<name>/cuisines/<id>', user_rest_cuisine, name="user_rest_cuisine"),
  path('Checkout/', Checkout, name="Checkout"),
  path('add-to-cart/', add_to_cart, name="add_to_cart"),
  path('update-cart/', update_cart, name="update_cart"),
  path('remove-cart/', remove_cart, name="remove_cart"),
]