from django.urls import path
from . import views


app_name = 'output'

urlpatterns = [
    path('', views.output, name='output'),
    path('<str:selected_district>/<str:selected_industry>/<str:neighborhood_code>/<int:group_id>/sales', views.group_detail_sales, name='sales'),
    path('<str:selected_district>/<str:selected_industry>/<str:neighborhood_code>/<int:group_id>/floating', views.group_detail_floating, name='floating'),
    path('<str:selected_district>/<str:selected_industry>/<str:neighborhood_code>/<int:group_id>/living', views.group_detail_living, name='living'),
    path('<str:selected_district>/<str:selected_industry>/<str:neighborhood_code>/<int:group_id>/facility', views.group_detail_facility, name='facility'),
]
