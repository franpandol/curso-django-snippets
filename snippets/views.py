from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from braces.views import (
    GroupRequiredMixin,
    LoginRequiredMixin,
)
from .models import Snippet


class WebIndex(TemplateView):
    template_name = 'snippets/index.html'

    def get_context_data(self, *args, **kwargs):
        # Indicar contenido a mostrar en la página inicial.
        context = super(WebIndex, self).get_context_data(*args, **kwargs)
        
        snippets = Snippet.objects.all()
        context['snippets'] = snippets
        
        #context['fecha'] = fecha
        return context

class AboutUs(TemplateView):
    template_name = 'snippets/about_us.html'


class SnippetsList(ListView):
    """ Lista de trámites.  Búsqueda de trámites  """
    model = Snippet
    template_name = 'snippets/list.html'
    #paginate_by = 20


    def get_context_data(self, *args, **kwargs):
        context = super(SnippetsList, self).get_context_data(*args, **kwargs)
        snippets_count = len(Snippet.objects.all())
        context['snippets_count'] = snippets_count
        #context['snippets_list_start_p'] = self.model.objects.filter(titulo__startwith='P')
        return context

    def get_queryset(self):
        result = self.model.objects.filter(publicado=True)
        return result


class SnippetsDetail(DetailView):
    """ Detalle de un trámite """
    model = Snippet
    template_name = 'snippets/detail.html'


    def get_context_data(self, *args, **kwargs):
        context = super(SnippetsDetail, self).get_context_data(*args, **kwargs)
        return context
