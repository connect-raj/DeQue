from rest_framework import serializers
from Admin_Main.models import tables_data, cuisine_data, Order
from User_side.models import cart

class TableSerializer(serializers.ModelSerializer):
  class Meta:
    model = tables_data
    fields = '__all__'


class CuisinesSerializer(serializers.ModelSerializer):
  class Meta:
    model = cuisine_data
    fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
  class Meta:
    model = cart
    fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'