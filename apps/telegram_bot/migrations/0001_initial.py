# Generated by Django 5.0 on 2023-12-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=100, verbose_name='ID пользователя telegram')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('chat_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Чат ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
            ],
            options={
                'verbose_name': 'Пользователь телеграм',
                'verbose_name_plural': 'Пользователи телеграма',
            },
        ),
    ]
