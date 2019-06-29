from django.db import models

class Categoria(models.Model):
    class Meta:
        db_table = 'tb_categoria'

    id = models.AutoField(primary_key=True, editable=False, auto_created=True)
    titulo = models.CharField(max_length=50, unique=True)
    icone = models.URLField(max_length=255)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    aprovado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True) 

    database = 'db_loja_virtual'

    def __str__(self):
        return self.titulo
