# Generated by Django 3.1.2 on 2020-10-14 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_movies_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]