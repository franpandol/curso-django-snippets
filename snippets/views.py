from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import (
    GroupRequiredMixin,
    FormMessagesMixin,
    LoginRequiredMixin,
)
from .models import Snippet
from .forms import SnippetsFormulario

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


# http://django-braces.readthedocs.io/en/latest/form.html#formmessagesmixin

# Esta clase sirve para definir valores comunes para otras clases que hereden de esta
# Por ej. el template_name para SnippetsAlta y SnippetsUpdate es el mismo, asi como
# varios otros atributos. Por eso, escribo una clase que englobe este comportamiento 
# compartido
class SnippetsFormMixin(FormMessagesMixin):
    model = Snippet
    template_name = 'snippets/snippets_form.html'
    #title_list = 'Lista de Snippets'
    #url_list = reverse_lazy('snippets:snippets-list')
    form_class = SnippetsFormulario
    #success_url = reverse_lazy('snippets:detail-list')
    form_invalid_message = 'Verifique el formulario'


    def get_success_url(self):
        return reverse('snippets:snippets-detail', kwargs={'pk': self.object.pk})

# https://docs.djangoproject.com/en/1.9/ref/class-based-views/generic-editing/#createview
class SnippetsAlta(SnippetsFormMixin, CreateView):
    title_form = 'Nuevo Snippet'

    def get_form_valid_message(self):
        return 'Snippet: "{0}" creado'.format(self.object)


class SnippetsActualizar(SnippetsFormMixin, UpdateView):
    title_form = 'Editar Snippet'

    def get_form_valid_message(self):
        return 'Snippet: "{0}" actualizado'.format(self.object)

