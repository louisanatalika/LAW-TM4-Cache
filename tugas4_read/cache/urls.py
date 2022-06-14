from django.urls import path
from . import views


urlpatterns = [
	path('<str:npm>/', views.read, name='read'),
]