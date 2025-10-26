from django.contrib import admin
from .models import Categoria, Receita

# Register your models here.
class Receitas(admin.ModelAdmin):
    list_display = ['titulo', 'categoria']
    search_fields = ['titulo']
    list_filter = ['data_criacao', 'categoria']

class Categorias(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

admin.site.register(Categoria, Categorias)
admin.site.register(Receita, Receitas)
