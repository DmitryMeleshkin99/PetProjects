# Generated by Django 3.1.7 on 2021-09-13 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210913_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='descrition',
            new_name='description',
        ),
    ]