from django.db import models


class Cafeteria(models.Model):
    id = models.AutoField(primary_key= True)
    clasificacion = models.CharField(max_length=30, blank= False, null = False)
    producto = models.CharField(max_length=30, blank= False, null = False)
    calorias = models.IntegerField()
    precio = models.IntegerField()
    image = models.CharField(max_length = 150, blank = False, null = False)
    
    
    
    
    
    