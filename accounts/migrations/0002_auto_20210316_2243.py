# Generated by Django 3.1.7 on 2021-03-16 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='is_asssociate',
            new_name='is_lawyer',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='is_par_legal',
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='is_partner',
        ),
    ]
