from django.db import models

# Create your models here.
class Cats(models.Model):
    class Meta:
        verbose_name = 'Кот'
        verbose_name_plural = 'Коты'
        ordering = ['-age']

    name = models.CharField(max_length=50, verbose_name = 'Имя')
    age = models.PositiveIntegerField(verbose_name = 'Возраст')
    breed = models.CharField(max_length=50, verbose_name = 'Порода')
    hairiness = models.CharField(max_length=50, verbose_name = 'Волосатость')
    image = models.ImageField(upload_to='media/cats', verbose_name = 'Фото')

    def __str__(self):
        return self.name