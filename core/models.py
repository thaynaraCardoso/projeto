from django.db import models

# Create your models here.
class Questao(models.Model):
    id=models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=100)
    pergunta=models.TextField()
    opcao1=models.TextField()
    opcao2=models.TextField()
    opcao3=models.TextField()
    opcao4=models.TextField()
    correta = models.CharField(max_length=1)
    msg_correta = models.TextField()
    msg_errada = models.TextField()
    msg_neutra = models.TextField()

    def __str__(self):
        return self.titulo #Método para formatar a exibição dodado no banco de dados