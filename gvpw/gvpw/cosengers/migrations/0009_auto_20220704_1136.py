# Generated by Django 3.1.4 on 2022-07-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosengers', '0008_newblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newblog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='newevent',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]