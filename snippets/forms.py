from django import forms
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions, FieldWithButtons, StrictButton
from crispy_forms.layout import Submit, Layout, HTML, Button, Div

from .models import Snippet 

class SnippetsFormulario(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = (
            'titulo',
            'codigo',
            'lenguaje',
            'publicado',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div(
                   'titulo',
                   'codigo',
                   'lenguaje',
                   'publicado',
                    #Fieldset('Redes Sociales', redes_sociales),
                    #Fieldset('Información Extra', fechas_institucion_fields),
                    css_class='col-md-12 col-lg-12'
                ),
                css_class='row '
            )
        )

        #Listar todos los campos con el diseño por defecto
        #self.helper.layout = Layout(*list(self.fields))
        self.helper.layout.append(
            FormActions(
                Button('cancel', 'Cancelar', css_class='btn-default', onclick="window.history.back()"),
                Submit('save', 'Guardar'),
            )
        )

class QSearchFormSnippets(forms.Form):
    
    q = forms.CharField()


    def __init__(self, *args, **kwargs):
        super(QSearchFormSnippets, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'get'

        self.helper.form_action = '.'
        self.helper.layout = Layout(
            FieldWithButtons(
                'q',
                StrictButton(
                    _('Buscar por titulo del snippet'),
                    type='submit',
                    css_class='btn btn-primary'
                )
            )
        )
