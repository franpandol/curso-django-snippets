from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from braces.views import (
    GroupRequiredMixin,
    LoginRequiredMixin,
)

class WebIndex(TemplateView):
    template_name = 'snippets/index.html'

    def get_context_data(self, *args, **kwargs):
        # Indicar contenido a mostrar en la página inicial.
        snippets = Snippet.objects.all()
        context = super(WebIndex, self).get_context_data(*args, **kwargs)
        context['snippets'] = snippets
        return context
