# Generated by Django 2.0.9 on 2018-12-13 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=0, verbose_name='Situação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('pacote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to='pacotes.Pacote', verbose_name='Pacote')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
        ),
        migrations.AlterUniqueTogether(
            name='inscricao',
            unique_together={('user', 'pacote')},
        ),
    ]