# Generated by Django 4.1.6 on 2023-02-13 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jouer', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='mot',
        ),
        migrations.RenameField(
            model_name='mot',
            old_name='mot',
            new_name='text',
        ),
    ]
