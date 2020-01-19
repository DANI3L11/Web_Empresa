from django.contrib import admin
from .models import Products


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Products, ProductAdmin)

# Register your models here.
