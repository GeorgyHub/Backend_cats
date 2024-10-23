from django.db import models

# Create your models here.
class Cats(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Имя')
    age = models.PositiveIntegerField(verbose_name = 'Имя')
    breed = models.CharField(max_length=50, verbose_name = 'Имя')
    hairiness = models.CharField(max_length=50, verbose_name = 'Имя')

    def __str__(self):
        return self.name