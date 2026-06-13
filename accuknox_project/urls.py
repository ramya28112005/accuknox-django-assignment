from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('signals_demo.urls')),
    path('admin/', admin.site.urls),
]