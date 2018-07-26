from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Fotolito(models.Model):
    FINALIDADE_CHOICES = (
        ('OFFSET', 'Impressão Off Set'),
        ('VERNIZ', 'Reserva Verniz'),
        ('SILK', 'Silk Scren'),
    )
    CAMADA_CHOICES = (
        ('LEGIVEL', 'Legível'),
        ('ILEGIVEL', 'Ilegível'),
    )
    LINEATURA_CHOICES = (
        ('40', '40'),
        ('60', '60'),
        ('80', '80'),
        ('100', '100'),
        ('120', '120'),
        ('150', '150'),
        ('175', '175'),
        ('200', '200'),
    )
    APROVACAO_CHOICES = (
        ('NÃO', 'Excluir processo de aprovação'),
        ('SIM', 'Quero receber um PDF final para aprovação'),
    )
    titulo = models.CharField(max_length=100)
    altura = models.CharField(max_length=10)
    largura = models.CharField(max_length=10)
    cores = models.CharField(max_length=10)
    finalidade = models.CharField(max_length=20,
                                  choices=FINALIDADE_CHOICES,
                                  default='OFFSET')
    camada = models.CharField(max_length=20,
                              choices=CAMADA_CHOICES, default='LEGIVEL')
    lineatura = models.CharField(max_length=10,
                                 choices=LINEATURA_CHOICES, default='175')
    arquivo = models.FileField(upload_to='documents/%Y/%m/%d/')
    recomendacoes = models.TextField()
    aprovacao = models.CharField(max_length=50,
                                 choices=APROVACAO_CHOICES, default='NÃO')
    added_by = models.ForeignKey(User,
                                 blank=True, null=True,
                                 on_delete=models.SET_NULL)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Fotolitos"

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
