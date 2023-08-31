from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
'''admin.site.register(Size)'''

'''class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','brand','color','status')
    list_editable = ('status',)
admin.site.register(Product,ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','product','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)'''


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    model = Size


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'detail', 'category', 'brand', 'price', 'color', 'status')
    inlines = [ProductImageAdmin]


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
