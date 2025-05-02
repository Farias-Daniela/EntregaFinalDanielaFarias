from django.contrib import admin
from .models import Message
from django.contrib import admin
from .models import Product, ProductImage

admin.site.register(Message)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
