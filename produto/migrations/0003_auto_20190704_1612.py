# Generated by Django 2.2.2 on 2019-07-04 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_produto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.IntegerField(),
        ),
    ]
