from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с необходимыми правами'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Модератор продуктов')
        permissions = [
            Permission.objects.get(codename='can_unpublish_product'),
            Permission.objects.get(codename='delete_product')
        ]
        group.permissions.set(permissions)
        self.stdout.write(self.style.SUCCESS(f'Группа "Модератор продуктов" успешно создана и настроена'))
