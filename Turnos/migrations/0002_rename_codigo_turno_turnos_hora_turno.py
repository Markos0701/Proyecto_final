# Generated by Django 4.1.3 on 2023-01-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Turnos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turnos',
            old_name='Codigo_Turno',
            new_name='hora_Turno',
        ),
    ]
