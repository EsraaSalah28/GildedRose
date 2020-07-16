from django.db import models

# Create your models here.
class Item(models.Model):
    itemId=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    sellIn=models.FloatField()
    qaulityValue=models.IntegerField()
    itemType = models.CharField(max_length= 20, default='reg')