from django.contrib import admin
from django.utils.text import slugify
from django.utils import timezone
from shop.models import Category, Product, SlideShow
from parler.admin import TranslatableAdmin


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = (
        'id',
        'title',
        'is_sub',
        'created',

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
        'id',
        'created'
    )
    list_per_page = 20

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        return super().save_model(request, obj, form, change)


@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'category',
        'image',
        'price',
        'available',
        'created',
        'updated'
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'category', 'available', 'created', 'updated'
    )
    search_fields = (
        'title', 'slug', 'description'
    )
    list_editable = (
        'price', 'available'
    )
    list_per_page = 10
    list_select_related = (
        'category',
    )
    autocomplete_fields = (
        'category',
    )
    list_per_page = 20

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        return super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('category')


@admin.register(SlideShow)
class SlideShowAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'date_created',
    )
    list_display_links = (
        'id',
        'title',
    )
    list_filter = (
        'date_created',
    )
    search_fields = (
        'title',
    )
    list_per_page = 10
    date_hierarchy = 'date_created'
    readonly_fields = (
        'date_created',
    )

    def save_model(self, request, obj, form, change):
        if not obj.date_created:
            obj.date_created = timezone.now()
        return super().save_model(request, obj, form, change)
