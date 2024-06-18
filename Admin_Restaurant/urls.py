from django.urls import path
from .views import *

urlpatterns = [
  path('admin-rest/login/', res_login, name="res_login"),
  path('admin-rest/logout/', res_logout, name="res_logout"),
  path('admin-rest/home/', rest_home, name="rest_home"),
  path('admin-rest/cuisines/', rest_cuisines, name="rest_cuisines"),
  path('admin-rest/cuisines/add', add_cuisines, name="rest_cuisines"),
  path('admin-rest/cuisines/Activate/<id>', status_activate, name="status_activate"),
  path('admin-rest/cuisines/InActivate/<id>', status_deactivate, name="status_deactivate"),
  path('admin-rest/cuisines/update/<id>', cuisine_update, name="cuisine_update"),
  path('admin-rest/tables/', rest_table_view, name="rest_table_view"),
  path('admin-rest/tables/add', add_table, name="rest_table"),
  path('admin-rest/tables/Maintainence/<id>', status_maintain, name="status_maintain"),
  path('admin-rest/tables/Reserve/<id>', status_reserve, name="status_reserve"),
  path('admin-rest/tables/Active/<id>', status_active, name="status_active"),
]