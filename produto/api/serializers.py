from rest_framework.serializers import ModelSerializer, ValidationError

from categoria.models import Categoria
from produto.models import Produto


class ProdutoSerializer(ModelSerializer):

    class Meta:
        model = Produto
        fields = ('id', 'titulo', 'categoria', 'descricao', 'preco')
        ordering = ['titulo', ]

    def insere(self, data):
        try:
            serializer = ProdutoSerializer(titulo=data['titulo'],
                                           categoria=int(data['categoria']),
                                           descricao=data['descricao'],
                                           preco=float(data['preco']))
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return serializer.data
        except Exception as e:
            raise ValidationError({'error': e})

    def atualiza(self, id, data):
        try:
            produto = Produto.objects.get(pk=id)

            categoria = Categoria.objects.get(id=data['categoria'])

            serializer = ProdutoSerializer(produto, data={
                'titulo': data['titulo'],
                'categoria': int(data['categoria']),
                'descricao': data['descricao'],
                'preco': float(data['preco'])},
                partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return serializer.data
        except Exception as e:
            raise ValidationError({'error': e})


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
