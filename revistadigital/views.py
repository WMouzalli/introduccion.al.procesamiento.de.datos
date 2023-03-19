from django.shortcuts import render
from multiprocessing import context
from re import template
from .models import Post
from django.views.generic import TemplateView

class home(TemplateView):
    template_name="revistadigital/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

def integrantes(request):
    return render(request, 'revistadigital/integrantes.html')

def bibliografia(request):
    return render(request, 'revistadigital/bibliografia.html')