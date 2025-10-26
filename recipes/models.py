from django.db import models

# Create your models here.
class Categoria(models.Model): # Cria a classe "Categoria"
    nome = models.CharField(max_length=25) # Nome da categoria

    def __str__(self): # Representação em string da categoria
        return self.nome # Nome da categoria

class Receita(models.Model): # Cria a classe "Receita"
    titulo = models.CharField(max_length=100) # Título da receita
    ingredientes = models.TextField() # Ingredientes da receita
    modo_preparo = models.TextField() # Modo de preparo da receita
    data_criacao = models.DateTimeField(auto_now_add=True) # Data de criação da receita
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # Categoria da receita

    def __str__(self): # Representação em string da receita
        return self.titulo # Título da receita