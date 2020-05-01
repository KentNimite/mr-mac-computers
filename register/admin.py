from django.contrib import admin
from .models import HomePage, ShoppingItem, Gallery


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'page_paragraph')
    ordering = ('update_date',)
    search_fields = ('page_title',)
admin.site.register(HomePage, HomePageAdmin)


class ShoppingItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'paystack_url', 'item_description')
    ordering = ('priority_level', 'item_name')
    search_fields = ('item_name',)
admin.site.register(ShoppingItem, ShoppingItemAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name_of_item', 'date_added', 'photo')
    ordering = ('date_added',)
    search_fields = ('name_of_item',)
admin.site.register(Gallery, GalleryAdmin)




