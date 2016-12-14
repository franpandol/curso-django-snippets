from django.shortcuts import render

from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin
from snippets.models import Snippet

# Create your views here.
class WebIndex(LoginRequiredMixin, TemplateView):
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        # Indicar contenido a mostrar en la página inicial.
        context = super(WebIndex, self).get_context_data(*args, **kwargs)
        
        snippets = Snippet.objects.all()
        context['snippets'] = snippets
        
        #context['fecha'] = fecha
        return context

class AboutUs(TemplateView):
    template_name = 'web/about_us.html'
