from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from apps.chat.models import Room, Messages

# Create your views here.

def getHome(request):
	salas = Room.objects.all()
	context = {
		"salas": salas
	}	
	return render(request, 'chat/home.html', context)

def getRoom(request, room_name):	
	sala = Room.objects.filter(nombre = room_name)
	if len(sala) == 1:
		mensajes = Messages.objects.filter(sala = sala[0]).order_by('-fecha')[:50:-1]
		context = {
			"mensajes": mensajes,
			"room_name_json": mark_safe(json.dumps(room_name))
		}
		return render(request, 'chat/room.html', context)
	else:
		return render(request, 'chat/404.html')