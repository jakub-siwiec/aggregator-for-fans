# Generated by Django 3.1.2 on 2020-10-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0009_auto_20201016_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]