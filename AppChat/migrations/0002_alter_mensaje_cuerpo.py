# Generated by Django 4.1.3 on 2023-01-29 16:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppChat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
