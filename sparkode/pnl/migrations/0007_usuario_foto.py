# Generated by Django 2.2.3 on 2020-01-17 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnl', '0006_auto_20200109_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Foto',
            field=models.ImageField(null=True, upload_to='perfil'),
        ),
    ]
