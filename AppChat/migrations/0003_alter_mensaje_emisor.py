# Generated by Django 4.1.3 on 2023-01-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppChat', '0002_alter_mensaje_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='emisor',
            field=models.CharField(max_length=150),
        ),
    ]
