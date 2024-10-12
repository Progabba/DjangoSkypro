from django import template

register = template.Library()

@register.filter()
def media_filter(path):
    if path:
        # Проверка, что путь уже не начинается с '/media/'
        if not path.startswith('/media/'):
            return f'/media/{path}'
        return path
    return '#'
