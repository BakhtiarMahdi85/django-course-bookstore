from django.urls import path
from .views import HomePage_view

urlpatterns = [
    path('', HomePage_view.as_view(), name='home'),
]