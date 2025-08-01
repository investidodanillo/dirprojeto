# Generated by Django 5.1.1 on 2025-03-30 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tabela1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(db_index=True, max_length=150)),
                ('campo2', models.SlugField(max_length=150, unique=True)),
                ('campo3', models.TextField(choices=[('S', 'SIM'), ('N', 'NÃO')], max_length=150)),
                ('campo4', models.BooleanField(default=False, help_text='Exemplo de BooleanField.', verbose_name='Campo Booleano')),
                ('campo5', models.TextField(help_text='Exemplo de TextField.', verbose_name='Campo de Texto Longo')),
            ],
            options={
                'indexes': [models.Index(fields=['campo1'], name='aplicativo__campo1_71cb54_idx')],
            },
        ),
    ]
