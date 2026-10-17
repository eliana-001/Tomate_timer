from django.urls import path
from . import views

app_name = 'metas'

urlpatterns = [
    path('', views.index, name='index'),
]
