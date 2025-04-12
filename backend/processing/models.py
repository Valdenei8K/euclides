from django.db import models

class StatusProcessamento(models.TextChoices):
    PROCESSANDO = 'Processando', 'Processando'
    CONCLUIDO = 'Concluído', 'Concluído'

class Processamento(models.Model):
    numeros_csv = models.TextField()  

    media = models.FloatField(null=True, blank=True)
    mediana = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=StatusProcessamento.choices,
        default=StatusProcessamento.PROCESSANDO
    )

    criado_em = models.DateTimeField(auto_now_add=True)

    @property
    def numeros(self):
        return [float(n) for n in self.numeros_csv.split(',') if n.strip()]

    @numeros.setter
    def numeros(self, lista):
        self.numeros_csv = ','.join(str(n) for n in lista)

    def __str__(self):
        return f'Processamento #{self.pk}'
