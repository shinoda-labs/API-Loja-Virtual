from rest_framework.viewsets import ModelViewSet
from produto.models import Produto
from categoria.models import Categoria
from produto.api.serializers import ProdutoSerializer, ProdutoAdmSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class ProdutoViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'delete', 'post']
    serializer_class = ProdutoSerializer
    filter_fields = ['categoria', ]

    def get_queryset(self):
        return Produto.objects.filter(aprovado=True, ativo=True).order_by('titulo')

    def create(self, request, *args, **kwargs):
        produto = ProdutoSerializer().insere(request.data)
        return Response(data=produto, status=200)

    def partial_update(self, request, *args, **kwargs):
        produto = ProdutoSerializer().atualiza(id=kwargs['pk'], data=request.data)

        return Response(data=produto, status=200)

    @action(methods=['patch'], detail=True)
    def aprovar(self, request, pk):
        produto = ProdutoAdmSerializer().aprovar(pk)
        return Response(data=produto, status=200)

    @action(methods=['patch'], detail=True)
    def reprovar(self, request, pk):
        produto = ProdutoAdmSerializer().reprovar(pk)
        return Response(data=produto, status=200)

    @action(methods=['patch'], detail=True)
    def ativar(self, request, pk):
        produto = ProdutoAdmSerializer().ativar(pk)
        return Response(data=produto, status=200)

    @action(methods=['patch'], detail=True)
    def inativar(self, request, pk):
        produto = ProdutoAdmSerializer().inativar(pk)
        return Response(data=produto, status=200)
