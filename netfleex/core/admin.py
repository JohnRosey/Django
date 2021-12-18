from django.contrib import admin
from django.db import models
from django.db.models import fields
from tinymce.widgets import TinyMCE 
from .models import Category, Netfeelex

# Register your models here.
choices=Category.objects.all()
class NetfeelexAdmin(admin.ModelAdmin):
    fields = ['Titre_film', 'Contenu_film', 'Date_publication', 'Category']
    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()},
    }
    
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
admin.site.register(Category, CategoryAdmin)  
admin.site.register(Netfeelex)