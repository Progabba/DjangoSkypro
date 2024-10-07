from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Удаляет все продукты и категории и добавляет тестовые данные либо вручную, либо через фикстуры."

    def add_arguments(self, parser):
        # Аргумент для использования фикстур
        parser.add_argument(
            '--use-fixtures',
            action='store_true',
            help='Загрузить данные из фикстур вместо создания вручную'
        )

    def handle(self, *args, **kwargs):
        use_fixtures = kwargs['use_fixtures']

        # Удаление всех продуктов и категорий
        Product.objects.all().delete()
        Category.objects.all().delete()

        if use_fixtures:
            # Загрузка данных из фикстур
            call_command('loaddata', 'categorys_fixture.json')
            call_command('loaddata', 'products_fixture.json')
            self.stdout.write(self.style.SUCCESS('Данные загружены из фикстур!'))
        else:
            # Вручную добавляем тестовые категории
            category1 = Category.objects.create(name="Категория 1", discription="Описание категории 1")
            category2 = Category.objects.create(name="Категория 2", discription="Описание категории 2")

            # Вручную добавляем тестовые продукты
            Product.objects.create(
                name="Продукт 1",
                discription="Описание продукта 1",
                price=1000,
                category=category1,
            )
            Product.objects.create(
                name="Продукт 2",
                discription="Описание продукта 2",
                price=1500,
                category=category1,
            )
            Product.objects.create(
                name="Продукт 3",
                discription="Описание продукта 3",
                price=2000,
                category=category2,
            )

            self.stdout.write(self.style.SUCCESS('Тестовые данные добавлены вручную!'))
