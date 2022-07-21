from django.urls import path, include
from . import views

urlpatterns = [
  path('tokens/', views.index, name='index'),
]
