from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_neighborhood, name='input_neighborhood'),
]