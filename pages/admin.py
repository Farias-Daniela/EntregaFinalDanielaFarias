from django.contrib import admin
from .models import Page, PageImage

class PageImageInline(admin.TabularInline):  
    model = PageImage
    extra = 20

class PageAdmin(admin.ModelAdmin):
    inlines = [PageImageInline]  

admin.site.register(Page, PageAdmin)