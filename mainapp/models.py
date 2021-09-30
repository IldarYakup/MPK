from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название профессии', max_length=128)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(verbose_name='Цена продукта', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name}{self.category.name}"