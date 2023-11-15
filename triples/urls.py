from django.contrib import admin
from django.urls import path, include
from output import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('input/', views.input),
    path('output/', include('output.urls')),
]
