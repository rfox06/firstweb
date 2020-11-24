from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
    CreateView
)
# import models tercer class

from .models import Prueba

from .forms import PruebaForm


class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

####


class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['1', '13', '20', '38']


class ListaPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'  # enlaza con aqui lista va en el template html


class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'
