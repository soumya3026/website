# Generated by Django 3.2 on 2022-04-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_fac_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fac',
            name='pic',
            field=models.ImageField(upload_to='./faculty/images/'),
        ),
    ]