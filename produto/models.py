from django.db import models

class Produto(models.Model):
    class Meta:
        db_table = 'tb_produto'
    
    id = models.AutoField(primary_key=True, editable=False, auto_Created=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)