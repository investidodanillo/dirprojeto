# dirprojeto\aplicativo\models\assunto02\models.py
from django.db import models

class Tabela1(models.Model):
    CONFIRMA = [
        ('S', 'SIM'),
        ('N', 'NÃO'),
    ]
    
    campo1 = models.CharField(max_length=150, db_index=True)
    campo2 = models.SlugField(max_length=150, unique=True, db_index=True)
    campo3 = models.CharField(max_length=1, choices=CONFIRMA)  # Alterado para CharField
    campo4 = models.BooleanField(default=False, verbose_name="Campo Booleano")
    campo5 = models.TextField(verbose_name="Campo de Texto Longo")

    class Meta:
        indexes = [
            models.Index(fields=['campo1']),
        ]
    
    def __str__(self):
        return self.campo1


