from django.urls import path
from . import views


app_name = 'output'

urlpatterns = [
    path('', views.output, name='output'),
    path('output/', views.output, name='output'),
    path('output/cluster_group/', views.cluster_group, name='cluster_group'),
    path('group_detail/<int:group_id>/', views.group_detail, name='group_detail'),
]
