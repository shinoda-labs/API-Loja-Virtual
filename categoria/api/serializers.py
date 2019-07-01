from rest_framework.serializers import ModelSerializer, ValidationError
from categoria.models import Categoria


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'titulo', 'icone')
        ordering = ['titulo', ]


class CategoriaProdutoSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('titulo',)
