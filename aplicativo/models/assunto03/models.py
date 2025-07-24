# dirprojeto\aplicativo\models\assunto03\models.py

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


#TIPO DE CAMPOS E ATRIBUTOS
class TabelaSis1(models.Model):
    campo1 = models.CharField(max_length=100, verbose_name="campo1: Campo de Texto Curto")
    campo2 = models.TextField(verbose_name="campo2: Campo de Texto Longo")
    campo3 = models.IntegerField(verbose_name="campo3: Número Inteiro")
    campo4 = models.FloatField(verbose_name="campo4: Número Decimal")
    campo5 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="campo5: Número Decimal Precisão Fixa")
    campo6 = models.BooleanField(default=False, verbose_name="campo6: Campo Booleano")
    campo7 = models.DateField(verbose_name="campo7: Data")
    campo8 = models.TimeField(verbose_name="campo8: Hora")
    campo9 = models.DateTimeField(verbose_name="campo9: Data e Hora")
    campo10 = models.EmailField(verbose_name="campo10: E-mail")
    campo11 = models.URLField(verbose_name="campo11: URL")
    campo12 = models.SlugField(verbose_name="campo12: Slug")
    campo13 = models.UUIDField(verbose_name="campo13: UUID")
    campo14 = models.BinaryField(verbose_name="campo14: Binário")
    campo15 = models.ImageField(upload_to="imagens/", verbose_name="campo15: Imagem")
    campo16 = models.FileField(upload_to="arquivos/", verbose_name="campo16: Arquivo")

    # Exemplos de atributos
    campo17 = models.CharField(
        max_length=50,
        unique=True,
        null=False,
        blank=False,
        verbose_name="campo17: Campo Único",
        help_text="Este campo deve ter um valor único."
    )
    campo18 = models.IntegerField(
        default=0,
        verbose_name="campo18: Campo com Valor Padrão",
        help_text="Este campo tem um valor padrão."
    )
    campo19 = models.CharField(
        max_length=20,
        choices=[
            ('A', 'Opção A'),
            ('B', 'Opção B'),
            ('C', 'Opção C'),
        ],
        verbose_name="campo18: Campo com Choices",
        help_text="Escolha entre as opções disponíveis."
    )

    # Exemplos de restrições de valores
    campo20 = models.PositiveIntegerField(
        verbose_name="campo20: Número Positivo",
        help_text="Apenas valores positivos são permitidos."
    )
    campo21 = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    verbose_name="campo21: Número entre 0 e 100",
    help_text="Insira um número entre 0 e 100.",
    validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
        ]
    )
    Campo22 = models.OneToOneField('TabelaSis2', on_delete=models.CASCADE, related_name='relacionado')

    def __str__(self):
        return f"ExemploModel (ID: {self.id})"

    class Meta:
        verbose_name = "Exemplo de Model"
        verbose_name_plural = "campo22: Exemplos de Models"
        ordering = ['campo1']  # Ordenação padrão



class TabelaSis2(models.Model):
    campo1 = models.CharField(max_length=100, verbose_name="campo1: Campo de Texto Curto")
    campo2 = models.IntegerField(verbose_name="Número Inteiro", help_text="Exemplo de IntegerField.")

    def __str__(self):
        return self.campo1  # Melhor para exibição no Django Admin


