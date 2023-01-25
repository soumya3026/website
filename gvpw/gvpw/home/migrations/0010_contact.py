# Generated by Django 3.2 on 2022-04-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_fac_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=200)),
                ('lname', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(default='', max_length=200)),
                ('msg', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
