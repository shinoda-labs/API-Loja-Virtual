from rest_framework.viewsets import ModelViewSet
from categoria.models import Categoria
from categoria.api.serializers import CategoriaSerializer, CategoriaAdmSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class CategoriaViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'delete', 'post']
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        return Categoria.objects.filter(aprovado=True, ativo=True).order_by('titulo')

    @action(methods=['patch'], detail=True)
    def aprovar(self, request, pk):
        produto = CategoriaAdmSerializer().aprovar(pk)
        return Response(data=produto, status=200)

    @action(methods=['patch'], detail=True)
    def reprovar(self, request, pk):
        produto = CategoriaAdmSerializer().reprovar(pk)
        return Response(data=produto, status=200)

    @action(methods=['patch'], detail=True)
    def ativar(self, request, pk):
        produto = CategoriaAdmSerializer().ativar(pk)
        return Response(data=produto, status=200)

    @action(methods=['patch'], detail=True)
    def inativar(self, request, pk):
        produto = CategoriaAdmSerializer().inativar(pk)
        return Response(data=produto, status=200)
