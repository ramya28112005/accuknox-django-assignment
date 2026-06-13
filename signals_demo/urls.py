from django.urls import path
from .views import test_signal_view

urlpatterns = [
    path('', test_signal_view),
]