# Generated by Django 4.1.3 on 2022-12-08 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMiembro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
