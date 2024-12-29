from django.contrib import admin
from ecommerce.models import Categoria, Produto

class Categorias(admin.ModelAdmin):
    list_display = ('id','nome', 'descricao','criado_em','atualizado_em')
    list_display_links = ('id','nome',)
    list_per_page = 20
    search_fields = ('nome', 'categoria')
    ordering = ('nome',)

admin.site.register(Categoria, Categorias)

class Produtos(admin.ModelAdmin):
    list_display = ('id','nome','descricao','preco','quantidade_estoque', 'categoria','imagem', 'criado_em','atualizado_em')
    list_display_links = ('id','nome')
    list_per_page = 20
    search_fields = ('nome', 'descricao')
    ordering = ('nome',)
admin.site.register(Produto, Produtos)