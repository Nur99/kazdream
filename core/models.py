from django.db import models

# Create your models here.


class Color(models.Model):
    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цветы'

    name = models.CharField(verbose_name='Название',
                            max_length=50)

    def __str__(self):
        return f'{self.name}'


class Manufacturer(models.Model):
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'

    name = models.CharField(verbose_name='Название',
                            max_length=50)

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    color = models.ForeignKey(Color,
                              related_name='cars',
                              on_delete=models.DO_NOTHING,
                              verbose_name='Цвет машины')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    manufacturer = models.ForeignKey(Manufacturer,
                                     related_name='cars',
                                     on_delete=models.DO_NOTHING,
                                     verbose_name='Производитель')

    def __str__(self):
        return f'{self.id}'
