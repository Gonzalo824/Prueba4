# Generated by Django 3.2.3 on 2021-07-05 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdjango', '0003_contacto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marca',
            new_name='Categoria',
        ),
        migrations.RenameModel(
            old_name='Producto',
            new_name='Libro',
        ),
    ]
