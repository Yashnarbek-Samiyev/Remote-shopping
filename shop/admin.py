from django.contrib import admin
from django.utils.text import slugify
from django.utils import timezone
from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created',
        'is_sub',
        
    )
    list_display_links = (
        'id',
        'title',
    )
    list_editable = (
        'is_sub',
    )
    list_filter = (
        'is_sub',
    )
    search_fields = (
        'title',
    )

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        return super().save_model(request, obj, form, change)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'price',
        'category',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'category',
    )
    search_fields = (
        'title', 'slug',
    )
    list_editable = (
        'price',
    )
    list_per_page = 10
    list_select_related = (
        'category',
    )
    autocomplete_fields = (
        'category',
    )
    save_as = True

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('category')