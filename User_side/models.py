from django.db import models

# Create your models here.
class cart(models.Model):
  product_id = models.IntegerField()
  quantity = models.IntegerField()
  user_name = models.CharField(max_length=30)
  status = models.CharField(max_length=20, default="incomplete")