from django.urls import path
from . import views

app_name = 'temporizador'

urlpatterns = [
    path('', views.index, name='index'),
]
