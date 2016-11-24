import django_tables2 as tables
from django_tables2.utils import A


class SnippetsTable(tables.Table):

    class Meta:
        attrs = {
            "class": "table table-striped table-bordered table-responsive"}

    titulo = tables.Column(verbose_name='Título')

    fecha_creacion = tables.Column(verbose_name='Fecha de creación')

    # controles = tables.TemplateColumn(
    #     template_name='snippets/list_controls.html',
    #     orderable=False
    # )
