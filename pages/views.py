from django.shortcuts import render
from django.views.generic.base import TemplateView
class HomePage_view(TemplateView):
    template_name = 'home.html'
