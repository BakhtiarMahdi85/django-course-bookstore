from django.urls import path
from. import views

urlpatterns = [
    path('',  views.signup_postView.as_view(), name='signup')
]
