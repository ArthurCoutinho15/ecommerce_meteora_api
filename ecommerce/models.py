from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=500, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.CharField(max_length=1000, blank=True)
    preco = models.DecimalField(max_digits=10,decimal_places=2, blank=False, null=False)
    quantidade_estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagem = models.ImageField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    