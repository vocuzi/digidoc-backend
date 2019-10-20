from django.urls import path
from app.views import *

urlpatterns = [
	path('login/', login),
	path('welcome/', welcome),
]
