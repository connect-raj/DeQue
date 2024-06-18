from rest_framework import serializers
from Admin_Main.models import cuisine_data, tables_data

class CuisineSerializers(serializers.ModelSerializer):
    # cuisine_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = cuisine_data
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
  class Meta:
    model = tables_data
    fields = '__all__'