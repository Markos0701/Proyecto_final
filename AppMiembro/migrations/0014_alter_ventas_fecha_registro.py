# Generated by Django 4.1.3 on 2023-01-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMiembro', '0013_ventas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='fecha_registro',
            field=models.DateField(blank=True, null=True),
        ),
    ]
