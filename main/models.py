from django.db import models


class MetaHotel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Назва мета готеля')

    class Meta:
        verbose_name = 'Мета готель'
        verbose_name_plural = 'Мета готелі'


def get_default_something():
    return {'history': []}


class Hotel(models.Model):
    name = models.CharField(max_length=32, verbose_name='Назва готеля')
    supplier_id = models.CharField(max_length=3, verbose_name='Поставщик')
    meta_hotel = models.ForeignKey(MetaHotel, null=True, blank=True, on_delete=models.SET_NULL, related_name='hotels')
    history = models.JSONField(null=True, blank=True, default=get_default_something)

    def __str__(self):
        return f"{str(self.id)}, {self.name}"

    class Meta:
        verbose_name = 'Готель'
        verbose_name_plural = 'Готелі'
