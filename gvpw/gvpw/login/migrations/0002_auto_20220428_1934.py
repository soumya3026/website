# Generated by Django 3.2 on 2022-04-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='is_cosenger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='face',
            name='is_picsl',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='face',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]