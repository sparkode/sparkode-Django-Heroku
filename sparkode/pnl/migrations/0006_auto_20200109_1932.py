# Generated by Django 3.0.2 on 2020-01-10 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnl', '0005_auto_20200103_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Nivel',
            field=models.CharField(max_length=2),
        ),
    ]
