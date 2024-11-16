from django.db import models
from django.conf import settings

from users.models import CustomUser


class Product(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Не опубликован'),
        ('published', 'Опубликован'),
    ]
    name = models.CharField(max_length=150, verbose_name="Название продукта")
    discription = models.TextField(verbose_name="Описание продукта", blank=True, null=True)
    image = models.ImageField(upload_to="catalog/image", blank=True, null=True, verbose_name="Изображение продукта")
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, verbose_name="Категория", blank=True, null=True, related_name='products'
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Статус публикации")
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        related_name="products",
        null=True,  # Разрешаем NULL временно
        blank=True
    ) # Новое поле

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]
        permissions = [
            ("can_unpublish_product", "Может отменять публикацию продукта")
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название категории")
    discription = models.TextField(
        verbose_name="Описание категории", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


# наименование,
# описание,
# изображение,
# категория,
# цена за покупку,
# дата создания,
# дата последнего изменения.
