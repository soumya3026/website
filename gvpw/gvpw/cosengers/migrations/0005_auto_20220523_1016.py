# Generated by Django 3.2 on 2022-05-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosengers', '0004_auto_20220516_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]