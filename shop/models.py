from django.db import models
from django.core.validators import FileExtensionValidator


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    image = models.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])],
        max_length=255,
        help_text='Изображение (jpg, png)'
    )
    sale_percent = models.IntegerField(verbose_name='Процент скидки', null=True, blank=True)
    white_name_sale = models.BooleanField(verbose_name='Белый цвет названия/скидки', default=False)
    show_in_slider = models.BooleanField(verbose_name='Показать в слайдере', default=False)
    is_recommended = models.BooleanField(verbose_name='Рекомендуемый товар', default=False)
    is_new_year_sale = models.BooleanField(verbose_name='Новогодняя скидка', default=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
