from django.urls import path
from . import views


app_name = 'output'

urlpatterns = [
    path('', views.output, name='output'),
    path('<str:selected_district>/<str:selected_industry>/<str:neighborhood_code>/<int:group_id>/', views.group_detail, name='group_detail'),
]
