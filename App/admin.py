from django.contrib import admin

# Register your models here.
from . models import Category, Varieties
from . models import Disease, CropVarieties
from . models import ProductCategory, ProductVarieties
from . models import CropCategory
from . models import Control, Symptom
from . models import CustomUser
admin.site.register(Category)
admin.site.register(CropCategory)
admin.site.register(ProductCategory)
admin.site.register(ProductVarieties)
admin.site.register(Control)
admin.site.register(Symptom)
admin.site.register(CustomUser)



class MyVariety(admin.ModelAdmin):
    list_display = ('category_var', 'name', 'date', 
                    'weather', 'yields', 'category', 'image')

admin.site.register(Varieties, MyVariety)

class MyCropVariety(admin.ModelAdmin):
    list_display = ('category_var', 'name', 'date',
                    'weather', 'yields', 'category', 'image')

admin.site.register(CropVarieties, MyCropVariety)

class MyDiseases(admin.ModelAdmin):
    list_display = ('name', 'date', 'pest_description','varieties')
admin.site.register(Disease, MyDiseases)



