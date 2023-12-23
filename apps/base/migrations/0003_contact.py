# Generated by Django 5.0 on 2023-12-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_about_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, verbose_name='email пользователя')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('cause', models.CharField(blank=True, max_length=100, null=True, verbose_name='Причина')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
        ),
    ]
