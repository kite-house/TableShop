from django.contrib import admin
from main.models import Products
# Register your models here.

class WatchProducts(admin.ModelAdmin):
    list_display = ('title', 'price', 'description')

admin.site.register(Products, WatchProducts)