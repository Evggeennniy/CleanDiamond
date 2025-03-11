from django.contrib import admin
from catalog.models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "category__name")
