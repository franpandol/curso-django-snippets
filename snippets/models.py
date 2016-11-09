
from django.db import models
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles

#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

LANGUAGE_CHOICES = (
	('PY', 'Python'),
	('JA', 'Java')
)

class Snippet(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=100, blank=True, default='')
    codigo = models.TextField()
    #linenos = models.BooleanField(default=False)
    lenguaje = models.CharField(choices=LANGUAGE_CHOICES, default=LANGUAGE_CHOICES[0][0], max_length=2)
    #estilo = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('fecha_creacion',)

    def __str__(self):
        return self.titulo