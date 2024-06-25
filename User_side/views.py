from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from Admin_Main.models import *
from User_side.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth import authenticate,login,logout
# Create your views here.


def signup(request):
  if request.method == "POST":
    username = request.POST['user_username']
    firstname = request.POST['user_firstname']
    lastname = request.POST['user_lastname']
    email = request.POST['user_email']
    password1 = request.POST['user_password1']
    password2 = request.POST['user_password2']

    if password1 == password2:
      data = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
      data.save()
      user = authenticate(username=username, password=password1)

      login(request, user)
      return redirect('home')
    else:
      return HttpResponse('Passwords not matching')
  return render(request,'signup.html')

def user_login(request):
  if request.method == "POST":
    username = request.POST['user_username']
    password = request.POST['user_password']

    user = authenticate(username=username, password=password)
    print(user)

    if user is not None:
      login(request, user)
      return redirect('/home')
    else:
      return redirect('signup')
  return render(request, 'login.html')

# @login_required
def user_home(request):
   return render(request, 'home.html')

def order(request):
   order_data = Order.objects.filter(User= request.user.id, OrderStatus= "Booked")
   context = {
      'order_data' : order_data
   }
   return render(request, "order.html", context=context)

def user_logout(request):
   logout(request)
   return redirect('home')

# @login_required
def user_restaurant(request):
  return render(request, "restaurants_page.html")

# @login_required
def restaurant_page(request, name):
  queryset = restaurants_data.objects.get(restaurant_name= name)

  context = {
    'queryset' : queryset
  }
  return render(request, "restaurant.html", context=context)

def layout_restaurant(request, name ):
  print(name)
  context = {
    "name" : name
  }
  return render(request, "../templates/layout_restaurant.html", context=context)

def user_rest_cuisine(request, name, id):
    print(name, id)
    request.session['SELECTED_TABLE_ID'] = int(id)
    print(request.session['SELECTED_TABLE_ID'])
    # print(cart_data)
    cart_data = cart.objects.filter(user_name=request.user)
    item_data = []
    for item in cart_data:
        cuisine = cuisine_data.objects.get(id=item.product_id)
        data = {
            'image': cuisine.cuisine_image,
            'price': cuisine.cuisine_price,
            'quantity': item.quantity
        }
        item_data.append(data)

    context = {
        'name': name,
        'cart_data': item_data
    }
    return render(request, 'cuisines.html', context=context)


# API Views Start Here >===>
@api_view(['GET'])
def fetch_tables(request, name):
  data = restaurants_data.objects.get(restaurant_name = name)
  res_admin = data.restaurant_admin
  table_data = tables_data.objects.filter(table_owner = res_admin).order_by('table_layout')
  print(tables_data,name)
  serializer = TableSerializer(data=table_data, many=True)
  if serializer.is_valid():
    return Response(serializer.data)
  else:
    return Response(serializer.data)
  
@api_view(['GET'])
def fetch_cuisines(request, name):
  data = restaurants_data.objects.get(restaurant_name = name)
  res_admin = data.restaurant_admin
  cuisines_data = cuisine_data.objects.filter(cuisine_restaurant_admin = res_admin)
  serializer = CuisinesSerializer(data=cuisines_data, many=True)
  if serializer.is_valid():
    return Response(name)
  else:
    return Response(serializer.data)
  


# Cart Section
def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")

        # Check if the product is already in the cart
        try:
            cart_item = cart.objects.get(product_id=product_id, user_name=request.user)
            cart_item.quantity += int(quantity)
            cart_item.save()
        except cart.DoesNotExist:
            # Product not in cart, create a new cart item
            cart_item = cart(
                product_id=product_id,
                quantity=quantity,
                user_name=request.user
            )
            cart_item.save()


            # Fetch updated cart data
            cart_data = cart.objects.filter(user_name=request.user)
            item_data = []
            for item in cart_data:
              cuisine = cuisine_data.objects.get(id=item.product_id)
              data = {
                'image': cuisine.cuisine_image,
                'price': cuisine.cuisine_price,
                'quantity': item.quantity
              }
              item_data.append(data)

            # Return the updated cart data as JSON response
            return JsonResponse(item_data, safe=False)

    return render(request, "cart.html")

@api_view(['GET'])
def fetch_cart(request):
   cart_data = cart.objects.filter(user_name=request.user)
   serializer = CartSerializer(data=cart_data, many=True)
   
   if serializer.is_valid():
      return Response(serializer.data)
   else:
      return Response(serializer.errors)
   
@csrf_exempt
def update_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        # Update the quantity in the database
        try:
            item = cart.objects.get(product_id=product_id)
            item.quantity = quantity
            item.save()
        except cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item not found'}, status=404)

        return JsonResponse({'success': True})

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def remove_cart(request):
   if request.method == "POST":
      product_id = request.POST.get("product_id")

      try:
         item = cart.objects.get(product_id=product_id)
         item.delete()  
      except cart.DoesNotExist:
         return JsonResponse({'error': 'Cart item not found'}, status=404)
      
      return JsonResponse({'success': True})
   
   return JsonResponse({'error': 'Invalid request'}, status=400)


# def Checkout(request):
   
#   if request.method == "POST":
#     Name = request.POST["FullName"]
#     UserName = request.user
#     PhoneNumber = request.POST["phone_number"]
#     NumberOfGuests = request.POST["number_of_guests"]
#     ExtraInstruction = request.POST["ExtraInstruction"]
#     TableID = request.session.get('SELECTED_TABLE_ID',0)

#     if TableID <= 0:
#       return redirect('/home')
#     else:
#       data = {
#         'User':Name,
#         'UserName':UserName,
#         'PhoneNumber':PhoneNumber,
#         'NumberOfGuests':NumberOfGuests,
#         'ExtraInstruction':ExtraInstruction,
#         'TableID':TableID
#       }

#       serializer = OrderSerializer(data=data, many=True)
#       if serializer.is_valid():
#          serializer.save()
#          table_data = tables_data.objects.get(id=TableID)
#          table_data.table_status = "Reserved"
#          table_data.save()
#          cart_data = cart.objects.filter(user_name=request.user)
#          for data in cart_data:
#            data.status = "complete"
#            data.save()
#       else: 
#          print(serializer.errors)
  
  
#   #cart page template
#   cart_data = cart.objects.filter(user_name=request.user)

#   data = []

#   for items in cart_data:
#     data_ = cuisine_data.objects.filter(id=items.product_id).first()
#     if data_:
#       data.append(data_)

#   context_data = zip(data, cart_data)


#   if request.session['SELECTED_TABLE_ID'] <= 0:
#      cart_data = cart.objects.filter(user_name=request.user, status="incomplete")
#      for data in cart_data:
#         data.delete()
#      return redirect('/home')
#   else:
#      table_data = tables_data.objects.get(id=request.session['SELECTED_TABLE_ID'])
#      user_data = User.objects.filter(username = request.user).first()


#      context = {
#        'user_data' : user_data,
#        'table_data' : table_data,
#        'context_data' : context_data
#     }

#      return render(request, "cart.html", context=context)

def Checkout(request):
    if request.method == "POST":
        UserName = request.POST["FullName"]
        PhoneNumber = request.POST["phone_number"]
        NumberOfGuests = request.POST["number_of_guests"]
        ExtraInstruction = request.POST["ExtraInstruction"]
        TableID = request.session.get('SELECTED_TABLE_ID', 0)
        UserId = request.user.id

        if TableID <= 0:
            return redirect('/home')
        else:
            data = {
                'User': UserId,
                'UserName': UserName,
                'PhoneNumber': PhoneNumber,
                'NumberOfGuests': NumberOfGuests,
                'ExtraInstruction': ExtraInstruction,
                'TableID': TableID
            }

            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                table_data = tables_data.objects.get(id=TableID)
                table_data.table_status = "Reserved"
                table_data.save()
                cart_data = cart.objects.filter(user_name=request.user)
                for item in cart_data:
                    item.status = "complete"
                    item.save()
                return redirect('/home')  # Redirect after successful order placement
            else:
                print(serializer.errors)
                return JsonResponse({'errors': serializer.errors}, status=400)

    # Cart page template
    cart_data = cart.objects.filter(user_name=request.user)
    data = []

    for item in cart_data:
        data_ = cuisine_data.objects.filter(id=item.product_id).first()
        if data_:
            data.append(data_)

    context_data = zip(data, cart_data)

    if request.session.get('SELECTED_TABLE_ID', 0) <= 0:
        cart_data = cart.objects.filter(user_name=request.user, status="incomplete")
        for item in cart_data:
            item.delete()
        return redirect('/home')
    else:
        table_data = tables_data.objects.get(id=request.session['SELECTED_TABLE_ID'])
        user_data = User.objects.filter(username=request.user).first()

        context = {
            'user_data': user_data,
            'table_data': table_data,
            'context_data': context_data
        }

        return render(request, "cart.html", context=context)