from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
	nombre = models.CharField(max_length = 50)

class Messages(models.Model):
	texto = models.TextField()
	fecha = models.DateTimeField(auto_now_add = True)
	sala = models.ForeignKey(Room, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
