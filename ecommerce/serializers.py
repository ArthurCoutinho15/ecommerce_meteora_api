from rest_framework import serializers
from ecommerce.models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
class ProdutoSerializer(serializers.ModelSerializer):
    # categoria = CategoriaSerializer(read_only=True)
    # categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source='categoria')
    class Meta:
        model = Produto
        exclude = []