from django.db import models
from categoria.models import Categoria


class Produto(models.Model):
    class Meta:
        db_table = 'tb_produto'

    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descricao = models.TextField(max_length=255)
    preco = models.FloatField()
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    database = 'db_loja_virtual'

    def __str__(self):
        return '{} - {}'.format(self.id, self.titulo)
