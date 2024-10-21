from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Product

# Контроллер для главной страницы
class HomeView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"

# Контроллер для страницы контактов
class ContactsView(View):
    template_name = "contacts.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")

# Контроллер для детальной страницы продукта
class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "product_id"



# def home(request):
#     products = Product.objects.all()
#     return render(request, "home.html", {"products": products})
#
#
# # def contacts(request):
# #     return render(request, 'contacts.html')
#
#
# def contacts(request):
#     if request.method == "POST":
#         # Получение данных из формы
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         # Обработка данных (например, сохранение в БД, отправка email и т. д.)
#         # Здесь мы просто возвращаем простой ответ
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, "contacts.html")
#
#
#
# def product_detail(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, "product_detail.html", {"product": product})