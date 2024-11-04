from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


from catalog.forms import ProductForm
from catalog.models import Product

# Контроллер для главной страницы
# class HomeView(ListView):
#     model = Product
#     template_name = "product_list.html"
#     context_object_name = "products"

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







class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')