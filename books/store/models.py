from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='стоимость')
    author = models.CharField(max_length=255, verbose_name='автор')

    def __str__(self):
        return f'{self.author}-{self.name}'
