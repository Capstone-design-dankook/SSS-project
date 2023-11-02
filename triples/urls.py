from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('input.urls')),
    path('input/', include('input.urls')),
    path('output/', include('output.urls')),
]
