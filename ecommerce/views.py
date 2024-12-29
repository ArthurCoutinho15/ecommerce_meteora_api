from ecommerce.models import Categoria, Produto
from ecommerce.serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'categoria', 'preco']