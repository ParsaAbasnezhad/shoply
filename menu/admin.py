from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "price", "stock", "category", "created_at")
    list_filter = ("type", "category")
    search_fields = ("name", "description")
