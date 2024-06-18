from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RestaurantSerializer
from .models import *

# Create your views here.
# def admin_login(request):

#   if request.method == 'POST':
#     admin_name = request.POST['admin_name']
#     admin_password = request.POST['admin_password']

#     admin = authenticate(username=admin_name, password=admin_password)

#     if admin is not None:
#       login(request, admin)
#       return redirect('/admin/dashboard')
#     else:
#       print("Wrong Credentials")

#   return render(request,'admin_login.html')



# @login_required('home/')
def admin_home(request):
  return render(request, 'admin_home.html')

def admin_restaurant_list(request):
  return render(request, 'restaurant_page.html')


def admin_login(request):
  if request.method == "POST":
    admin_name = request.POST['admin_name']
    admin_password = request.POST['admin_password']

    user = authenticate(username=admin_name, password=admin_password)
    print(user)

    if user is not None:
      login(request, user)
      return redirect('/admin/dashboard')
    
  return render(request, 'admin_login.html')

def admin_logout(request):
    logout(request)
    return redirect('/admin/login')

def add_rest(request):

  if request.method == 'POST':
      data = {
      'restaurant_name' : request.POST['restaurant_name'],
      'restaurant_admin_name' : request.POST['restaurant_admin_name'],
      'restaurant_password' : request.POST['restaurant_password'],
      'restaurant_phone_number' : request.POST['restaurant_phone_number'],
      'restaurant_email' : request.POST['restaurant_email'],
      'restaurant_address' : request.POST['restaurant_address'],
      'restaurant_image' : request.FILES.get('restaurant_image'),
      'restaurant_status' : request.POST.get('restaurant_status'),
      'restaurant_activation' : request.POST.get('activation'),
      }

      print(data)
      restaurant = restaurants_data.objects.create(
         restaurant_name = data['restaurant_name'],
         restaurant_admin = data['restaurant_admin_name'],
         restaurant_password = data['restaurant_password'],
         restaurant_phone_number = data['restaurant_phone_number'],
         restaurant_address = data['restaurant_address'],
         restaurant_email = data['restaurant_email'],
         restaurant_image = data['restaurant_image'],
         restaurant_status = data['restaurant_status'],
         restaurant_activity = data['restaurant_activation'],
      )

      restaurant.save()
      # data = request.POST.copy()
      # data["restaurant_image"] = request.FILES.get('restaurant_image')

      # serializer = RestaurantSerializer(data=data)
      # if serializer.is_valid():
      #    print(serializer.data)
      # else:
      #    print(serializer.errors)
      #    serializer.save()
      return redirect('/admin/restaurants/')

  return render(request, 'add-rest.html')

def Activate(request, id):
   queryset = restaurants_data.objects.get(id= id)
   queryset.restaurant_activity = True

   queryset.save()
   return redirect('/admin/restaurants/')

def Update(request, id):
   queryset = restaurants_data.objects.get(id= id)

   if request.method == "POST":
      data = request.POST.copy()
      

      queryset.restaurant_name = data["restaurant_name"]
      queryset.restaurant_address = data["restaurant_address"]
      queryset.restaurant_address = data["restaurant_address"]
      queryset.restaurant_email = data["restaurant_email"]
      queryset.restaurant_price_approx = data["restaurant_price_approx"]
      queryset.restaurant_active_time = data["restaurant_active_time"]
      queryset.restaurant_status = data["restaurant_status"]
    
      if request.FILES.get("restaurant_image"):
         queryset.restaurant_image = request.FILES.get("restaurant_image")


      queryset.save()
      return redirect('/admin/restaurants/')

   context = {
      "queryset" : queryset
   }
   return render(request, "admin_update_rest.html", context)

def open_rest(request, id):
   queryset = restaurants_data.objects.get(id=id)
   queryset.restaurant_status = "open"

   queryset.save()
   return redirect('/admin/restaurants/')

def close_rest(request, id):
   queryset = restaurants_data.objects.get(id=id)
   queryset.restaurant_status = "closed"

   queryset.save()
   return redirect('/admin/restaurants/')

@api_view(['GET'])
def get_restaurants(request):
   restaurants = restaurants_data.objects.all()
   serializer = RestaurantSerializer(restaurants, many=True)
   return Response(serializer.data)