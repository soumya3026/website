# Generated by Django 3.2 on 2022-05-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_profile', '0008_auto_20220526_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proffac',
            name='img',
            field=models.FileField(default='', upload_to='images/'),
        ),
    ]