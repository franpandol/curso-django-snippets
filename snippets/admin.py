from django.contrib import admin
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
	date_hierarchy = 'fecha_creacion'
	list_display = ('fecha_creacion', 'titulo',)
	list_filter = ('lenguaje',)
	search_fields = ['titulo', 'lenguaje']


admin.site.register(Snippet, SnippetAdmin)


#admin.site.register(Snippet)
