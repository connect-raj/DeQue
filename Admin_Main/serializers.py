from rest_framework import serializers
from .models import restaurants_data

class RestaurantSerializer(serializers.ModelSerializer):
  class Meta:
    model = restaurants_data
    # fields = ('restaurant_name','restaurant_admin','restaurant_password','restaurant_phone_number','restaurant_address','restaurant_email','restaurant_active_time','restaurant_status','restaurant_activity')
    fields = '__all__'