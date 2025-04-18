# Generated by Django 5.2 on 2025-04-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Processamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeros_csv', models.TextField()),
                ('media', models.FloatField(blank=True, null=True)),
                ('mediana', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Processando', 'Processando'), ('Concluído', 'Concluído')], default='Processando', max_length=20)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
