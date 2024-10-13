

from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='previews/', verbose_name="Превью", blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Признак публикации")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блоговая запись"
        verbose_name_plural = "Блоговые записи"

