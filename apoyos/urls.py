from django.urls import path
from . import views

app_name = 'apoyos'

urlpatterns = [
    path('', views.index, name='index'),
]
