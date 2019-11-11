from django.conf.urls import url
from apps.chat.views import *
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [
	path(r'home', login_required(getHome), name='home'),
	path(r'<str:room_name>/', login_required(getRoom), name='room'),
]