# Generated by Django 3.2 on 2022-05-24 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosengers', '0007_newevent'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=500)),
                ('img', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
