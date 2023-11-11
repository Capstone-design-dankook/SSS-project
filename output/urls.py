from django.urls import path
from . import views

app_name = 'output'

urlpatterns = [
    path('', views.input),
    path('input/', views.input),
    path('output/', views.input_district, name='output'),
]