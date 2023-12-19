from django.db import models

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length = 200,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Настройки сайта'
        verbose_name_plural='Настройки сайта'
