# Generated by Django 3.2.9 on 2021-11-14 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estado',
            old_name='siga',
            new_name='sigla',
        ),
    ]
