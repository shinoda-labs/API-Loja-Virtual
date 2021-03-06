from rest_framework.serializers import ModelSerializer, ValidationError
from categoria.models import Categoria
from rest_flex_fields import FlexFieldsModelSerializer


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'titulo', 'icone')
        ordering = ['titulo', ]


class CategoriaNestedSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Categoria
        fields = ('titulo',)


class CategoriaAdmSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'titulo', 'ativo', 'aprovado')

    def aprovar(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.aprovado is True:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'aprovado': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está aprovada.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})

    def reprovar(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.aprovado is False:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'aprovado': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está reprovada.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})

    def ativar(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.ativo is True:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'ativo': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está ativa.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})

    def inativar(self, id):
        flag = False
        try:
            categoria = Categoria.objects.get(pk=id)

            if categoria.ativo is False:
                flag = True
                raise
            else:
                serializer = CategoriaAdmSerializer(categoria, data={'ativo': False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return serializer.data
        except Exception as e:
            if flag:
                raise ValidationError({'error': 'A categoria {} já está inativa.'.format(id)})
            else:
                raise ValidationError({'error': 'Categoria inexistente'})