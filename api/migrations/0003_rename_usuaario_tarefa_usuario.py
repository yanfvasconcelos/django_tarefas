# Generated by Django 4.2.1 on 2023-05-11 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_descricso_tarefa_descricao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='usuaario',
            new_name='usuario',
        ),
    ]
