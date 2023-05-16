from django.contrib.auth import get_user_model
from django.db import models
from pyexpat import model

SITUACAO_CHOICES = [
    ('NOVA', 'NOVA'),
    ('EM ANDAMENTO', 'EM ANDAMENTO'),
    ('PENDENTE', 'PENDENTE'),
    ('RESOLVIDA', 'RESOLVIDA'),
    ('CANCELADA', 'CANCELADA')
]

User = get_user_model()

class Tarefa(models.Model):
    descricao = models.CharField()
    responsavel = models.CharField()
    nivel = models.IntegerField()
    prioridade = models.IntegerField()
    situacao = models.CharField(choices=SITUACAO_CHOICES)
    usuario = models.ForeignKey(
        User, related_name='tarefas', on_delete=models.SET_NULL, null=True, default=None
    )