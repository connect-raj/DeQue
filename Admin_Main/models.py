from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class restaurants_data(models.Model):
  restaurant_name = models.CharField(max_length=30, unique=True)
  restaurant_admin = models.CharField(max_length=30, unique=True)
  restaurant_password = models.CharField(max_length=20)
  restaurant_phone_number = models.CharField(max_length=12)
  restaurant_address = models.CharField(max_length=1000)
  restaurant_email = models.CharField(max_length=30)
  restaurant_image = models.ImageField(upload_to='uploads')
  restaurant_price_approx = models.CharField(max_length=30, default="1200/- for 2")
  restaurant_active_time = models.CharField(max_length=30, null=True)
  restaurant_status = models.CharField(default='closed', max_length=10)
  restaurant_activity = models.BooleanField(default=False, max_length=10)

class tables_data(models.Model):
  table_accomodation_type = models.IntegerField()
  table_owner = models.CharField(max_length=30)
  table_status = models.CharField(default="Active",max_length=20)
  table_layout = models.IntegerField(null = True)


class cuisine_data(models.Model):
  cuisine_name = models.CharField(max_length=30)
  cuisine_image = models.ImageField(upload_to='uploads')
  cuisine_type = models.CharField(max_length=50)
  cuisine_price = models.BigIntegerField()
  cuisine_status = models.CharField(max_length=10)
  cuisine_restaurant_admin = models.CharField(max_length=30)


class Order(models.Model):
  User = models.CharField(max_length=50)
  UserName = models.CharField(max_length=30, null=True)
  PhoneNumber = models.CharField(max_length=15)
  NumberOfGuests = models.IntegerField()
  TableID = models.IntegerField()
  ExtraInstruction = models.TextField(blank=True)
  CreatedAt = models.DateTimeField(auto_now_add=True)
  OrderStatus = models.CharField(max_length=50, default="Booked")
