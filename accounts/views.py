from django.shortcuts import render
from.form import CustomUserCreationForm
from.models import CustomUser
from django.views import generic
from django.urls import reverse_lazy
class signup_postView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/sigup.html'
    success_url = reverse_lazy('home')






