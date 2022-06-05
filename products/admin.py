"""Registration of Product and Category models """
from django.contrib import admin
from .models import Product, Category, SubCategory


class ProductAdmin(admin.ModelAdmin):
    """Product Admin"""
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'stock_qty',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    """Sub-category Admin"""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
