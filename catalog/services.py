from django.core.cache import cache
from .models import Product

def get_products_by_category(category_id, use_cache=True):
    if use_cache:
        cache_key = f'products_category_{category_id}'
        products = cache.get(cache_key)

        if not products:
            products = list(Product.objects.filter(category_id=category_id))
            cache.set(cache_key, products, 60 * 15)  # Кеш на 15 минут
        return products
    else:
        return Product.objects.filter(category_id=category_id)
