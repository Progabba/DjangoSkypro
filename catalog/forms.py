from django import forms
from .models import Product
from django.core.exceptions import ValidationError

# Запрещенные слова
FORBIDDEN_WORDS = [
    "казино", "криптовалюта", "крипта", "биржа",
    "дешево", "бесплатно", "обман", "полиция", "радар"
]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'discription', 'image', 'category', 'price']

    def clean(self):
        """Проверка на запрещенные слова в названии и описании."""
        cleaned_data = super().clean()
        name = cleaned_data.get("name", "")
        discription = cleaned_data.get("discription", "")

        for word in FORBIDDEN_WORDS:
            if word.lower() in name.lower() or word.lower() in discription.lower():
                raise ValidationError(
                    f"Запрещено использовать слово '{word}' в названии или описании."
                )
        return cleaned_data

    def clean_price(self):
        """Проверка, что цена не может быть отрицательной."""
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_image(self):
        """Проверка загружаемого изображения на формат и размер."""
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:
                raise ValidationError("Размер изображения не должен превышать 5 МБ.")
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise ValidationError("Допустимы только форматы JPEG и PNG.")
        return image

    def __init__(self, *args, **kwargs):
        """Стилизация формы."""
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',  # Единый CSS-класс для всех полей
                'placeholder': f'Введите {field.label.lower()}'
            })
