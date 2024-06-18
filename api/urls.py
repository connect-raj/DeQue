from django.urls import path
from Admin_Main.views import *
from Admin_Restaurant.views import *
from User_side.views import fetch_tables, fetch_cuisines, fetch_cart

urlpatterns = [
  path('get-restaurants/', get_restaurants, name="get_restaurants"),
  path('get-tables/', get_tables, name="get_tables"),
  path('get-cuisines/', get_cuisines, name="get_cuisines"),
  path('fetch-tables/<name>/', fetch_tables, name="fetch_tables"),
  path("fetch-cuisines/<name>/", fetch_cuisines, name="fetch_cuisines"),
  path("fetch-cart/", fetch_cart, name="fetch_cart")
]