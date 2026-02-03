from django.urls import path
from . import views
urlpatterns = [
    path('error', views.index, name='index'),
]