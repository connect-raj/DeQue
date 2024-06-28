from django.shortcuts import redirect, render
from Admin_Main.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from django.http import HttpResponse

# Create your views here.
##restaurant-admin login
def res_login(request):

  if request.method == "POST":
    adminrest_username = request.POST['adminrest_username']
    adminrest_password = request.POST['adminrest_password']

    admin_data = restaurants_data.objects.get(restaurant_admin= adminrest_username)

    try:
      user_data = User.objects.get(username= adminrest_username)
    except User.DoesNotExist:
      print("data not found")
      user_data = None

    if user_data is not None:
      user = authenticate(username=adminrest_username, password= adminrest_password)

      login(request, user)
      return redirect('/admin-rest/home')
    else:
      if admin_data.restaurant_password == adminrest_password:
        print(admin_data.restaurant_password)
        data = User.objects.create_user(username=adminrest_username, password=adminrest_password, email= admin_data.restaurant_email)
        data.is_staff = True
        data.save()

        user = authenticate(username=adminrest_username, password= adminrest_password)

        login(request, user)
        return redirect('/admin-rest/home')

      else:
        print("Error")

    
  return render(request, "adminres_login.html")

##admin home page
def rest_home(request):
  total_cuisines = cuisine_data.objects.filter(cuisine_restaurant_admin = request.user,cuisine_status = 'active').count()
  total_tables = tables_data.objects.filter(table_owner = request.user).count()
  tables = tables_data.objects.filter(table_owner=request.user.username)
  table_ids = [table.id for table in tables]
  total_orders = Order.objects.filter(TableID__in=table_ids).count()
  
  context = {
    "total_cuisines" : total_cuisines,
    "total_tables" : total_tables,
    "total_orders" : total_orders
  }
  return render(request, 'home_restadmin.html', context=context)


##Cuisine Views Start here
def rest_cuisines(request):
  print(request.user)
  return render(request, 'cuisines_rest_view.html')

def add_cuisines(request):
  
  if request.method == "POST":
      data = request.POST.copy()
      data["cuisine_image"] = request.FILES["cuisine_image"]
      print(data)
      serializer = CuisineSerializers(data=data)
      if serializer.is_valid():      
        serializer.save()
        print(serializer.data)
      else:
        print(serializer.errors)
    
    
  return render(request, "adminrest_add_cuisine.html")

#Update cuisine status==>
def status_activate(request, id):
  cuisine = cuisine_data.objects.get(id=id)
  cuisine.cuisine_status = "active"

  cuisine.save()
  return redirect('/admin-rest/cuisines')

def status_deactivate(request, id):
  cuisine = cuisine_data.objects.get(id=id)
  
  cuisine.cuisine_status = "inactive"

  cuisine.save()
  return redirect('/admin-rest/cuisines')
#Update cuisine status end


def cuisine_update(request, id):

    queryset = cuisine_data.objects.get(id=id)
    if request.method == "POST":
      data = request.POST.copy()
      image = request.FILES.get('cuisine_image')

      queryset.cuisine_name = data["cuisine_name"]
      queryset.cuisine_type = data["cuisine_type"]
      queryset.cuisine_price = data["cuisine_price"]
      queryset.cuisine_status = data["cuisine_status"]
      queryset.cuisine_restaurant_admin = data["cuisine_restaurant_admin"]

      if image:
        queryset.cuisine_image = image
      

      queryset.save()
      return redirect('/admin-rest/cuisines')
    
    context = {
      'queryset' : queryset
    }
    
    return render(request, "adminrest_update_cuisine.html", context)

@api_view(["GET"])
def get_cuisines(request):
  cuisines = cuisine_data.objects.filter(cuisine_restaurant_admin= request.user)
  serializer = CuisineSerializers(cuisines, many=True)
  return Response(serializer.data)
## End of Cuisine Views

##Order Views Start here

def rest_orders(request):
    # Get tables owned by the current restaurant admin
    tables = tables_data.objects.filter(table_owner=request.user.username)
    table_ids = [table.id for table in tables]

    # Filter orders that match these table IDs
    orders = Order.objects.filter(TableID__in=table_ids)
    data = []
    data2 = []

    message = 'Hey! This message is to inform that your Table will be ready in 30mins,we hope you reach their by the time being' 

    for order in orders:
        queryset = tables_data.objects.get(id=order.TableID)
        data.append(queryset)
        data2.append(order)

    context = {
        'dataset': zip(data2, data),
        'message': message
    }

    return render(request, "adminrest_order.html", context=context)

## End of Order Views

##Table Views Start here
def rest_table_view(request):
  return render(request, "tables_rest_view.html")

def add_table(request):

  if request.method == "POST":
    data = request.POST
    print(data)
    serializer = TableSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      print(serializer.errors)
      return redirect('/admin-rest/tables')
    else:
      print(serializer.data)  
      serializer.save()
      return redirect('/admin-rest/tables')
    

  return render(request, 'adminrest_add_table.html')

@api_view(['GET'])
def get_tables(request):
  tables = tables_data.objects.filter(table_owner = request.user)
  serializer = TableSerializer(tables, many=True)
  return Response(serializer.data)

#update table status==>
def status_maintain(request, id):
  data = tables_data.objects.get(id=id)
  data.table_status = "Maintainence"

  data.save()
  return redirect('/admin-rest/tables')


def status_reserve(request, id):
  data = tables_data.objects.get(id=id)
  data.table_status = "Reserved"

  data.save()
  return redirect('/admin-rest/tables')    


def status_active(request, id):
  data = tables_data.objects.get(id=id)
  data.table_status = "Available"

  data.save()
  return redirect('/admin-rest/tables')


#End for table status update
## End of Table Views

def res_logout(request):
  logout(request)
  return redirect('/admin-rest/login')