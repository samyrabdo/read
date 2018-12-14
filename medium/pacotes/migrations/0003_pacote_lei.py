# Generated by Django 2.0.9 on 2018-12-13 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leis', '0014_remove_lei_pacote'),
        ('pacotes', '0002_auto_20181213_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacote',
            name='lei',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='lei', to='leis.Lei', verbose_name='Lei'),
        ),
    ]