# Generated by Django 3.2 on 2022-05-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_profile', '0006_proffac'),
    ]

    operations = [
        migrations.AddField(
            model_name='proffac',
            name='desig',
            field=models.CharField(default='', max_length=100),
        ),
    ]