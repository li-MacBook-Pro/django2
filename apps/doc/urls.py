from django.urls import path, re_path

from . import views

app_name = 'doc'

urlpatterns = [
    path('index', views.index, name='index'),
]