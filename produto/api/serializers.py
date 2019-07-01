from rest_framework.serializers import ModelSerializer, ValidationError
from produto.models import Produto
from categoria.api.serializers import CategoriaProdutoSerializer


class ProdutoSerializer(ModelSerializer):
    categoria = CategoriaProdutoSerializer()

    class Meta:
        model = Produto
        fields = ('id', 'titulo', 'categoria', 'descricao', 'preco')
        ordering = ['titulo', ]


class ProdutoAdmSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ('id', 'titulo', 'ativo', 'aprovado')

    def aprovar(self, id):
        flag = False
        try:
            produto = Produto.objects.get(pk=id)

            if produto.aprovado is True:
                flag = True
                raise
            else:
                serializer = ProdutoAdmSerializer(produto, data={'aprovado': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O produto {} já está aprovado.'.format(id)})
            else:
                raise ValidationError({'error': 'Produto inexistente'})

    def reprovar(self, id):
        flag = False
        try:
            produto = Produto.objects.get(pk=id)

            if produto.aprovado is False:
                flag = True
                raise
            else:
                serializer = ProdutoAdmSerializer(produto, data={'aprovado': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O produto {} já está reprovado.'.format(id)})
            else:
                raise ValidationError({'error': 'Produto inexistente'})

    def ativar(self, id):
        flag = False
        try:
            produto = Produto.objects.get(pk=id)

            if produto.ativo is True:
                flag = True
                raise
            else:
                serializer = ProdutoAdmSerializer(produto, data={'ativo': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O produto {} já está ativo.'.format(id)})
            else:
                raise ValidationError({'error': 'Produto inexistente'})

    def inativar(self, id):
        flag = False
        try:
            produto = Produto.objects.get(pk=id)

            if produto.ativo is False:
                flag = True
                raise
            else:
                serializer = ProdutoAdmSerializer(produto, data={'ativo': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'O produto {} já está inativo.'.format(id)})
            else:
                raise ValidationError({'error': 'Produto inexistente'})