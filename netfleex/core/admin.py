from django.contrib import admin

from .models import Category, Netfeelex

# Register your models here.
admin.site.register(Netfeelex)
admin.site.register(Category)