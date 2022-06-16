from pyexpat import model
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    desc=models.CharField(max_length=255,default="old dojo")#can not add any thing with it 
    count=models.IntegerField(default=0)#used it to add num of id

class Ninja(models.Model):
    dojo_id=models.ForeignKey(Dojo,related_name="ninjas",on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    
