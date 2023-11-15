from django.urls import path
from . import views


app_name = 'output'

urlpatterns = [
    path('', views.input),
    path('output/', views.output, name='output'),
    path('output/distric', views.input_district, name='output'),
    path('output/cluster_group/', views.cluster_group, name='cluster_group'),
]