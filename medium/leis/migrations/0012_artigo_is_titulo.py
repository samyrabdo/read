# Generated by Django 2.1.4 on 2018-12-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leis', '0011_auto_20181206_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='is_titulo',
            field=models.BooleanField(blank=True, default=False, verbose_name='É título?'),
        ),
    ]