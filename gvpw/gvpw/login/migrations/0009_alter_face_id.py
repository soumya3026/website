# Generated by Django 3.2 on 2022-05-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_face_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]