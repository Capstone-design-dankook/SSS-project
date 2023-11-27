from django.contrib import admin
from django.urls import path, include
from output import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='first'),
    path('intro/', views.intro),
    path('industry/', views.industry),
    path('input/', views.input),
    path('output/', include('output.urls')),
]
