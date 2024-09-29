from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название продукта")
    discription = models.TextField(
        verbose_name="Описание продукта", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
    )
    category = models.ForeignKey('Category',
        on_delete=models.SET_NULL, verbose_name="Категория", blank=True, null=True,
        related_name='products',
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

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
