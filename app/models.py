from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser

class Nome(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
        
class Produto(models.Model):
    nome = models.ForeignKey(Nome, on_delete=models.SET_NULL, blank=True, null=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2) 
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome.nome
    

class carrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True)
    quantidade  = models.IntegerField()


class User(AbstractUser):
    pass

    def __str__(self):
        return self.username