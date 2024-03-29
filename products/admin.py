from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
# from tabbed_admin import TabbedModelAdmin
# from django.db import models
# from django.forms import TextInput, Textarea
from .models import Category, Product, Reviews, ProductImage, ImageHome, News, Status, SubCategory, Availability


class ProductAdminForm(forms.ModelForm):
    description_ru = forms.CharField(label='Описание [ru]', widget=CKEditorUploadingWidget())
    description_uk = forms.CharField(label='Описание [uk]', widget=CKEditorUploadingWidget())
    # description_ru = forms.Textarea()
    # description_uk = forms.Textarea()

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "get_image", )
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="50" height="auto">')

    get_image.short_description = "Изображение"
    readonly_fields = ("get_image", )


@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "get_image", )
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="50" height="auto">')

    get_image.short_description = "Миниатюра"
    readonly_fields = ("get_image", )


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 0
    readonly_fields = ("name", "email",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="auto">')

    get_image.short_description = "Изображение"

    readonly_fields = ("get_image", ) 


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ("id", "title", "get_image", "category", "dateAdd", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "draft", "material",)
    search_fields = ("id", "title", 'article',)
    save_on_top = True
    save_as = True
    actions = ['publish', 'unpublish']
    list_editable = ("draft",)

    prepopulated_fields = {"slug": ("title",)}

    form = ProductAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="auto">')
    
    get_image.short_description = "Изображение"

    readonly_fields = ("get_image", )
    
    inlines = [ProductImageInline, ReviewInline, ]

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        if row_update == 2:
            message_bit = '2 записи были обновлены'
        else:
            message_bit = f'{row_update} записей было обновлено'

        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 запись была обновлена'
        if row_update == 2:
            message_bit = '2 записи были обновлены'
        else:
            message_bit = f'{row_update} записей было обновлено'

        self.message_user(request, f"{message_bit}")


    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change', )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_image", "product",)
    list_display_links = ("title",)
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="auto">')

    get_image.short_description = "Изображение"



@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "text", "email", "product") # порядок отображения
    list_display_links = ("name",) # ссылка
    readonly_fields = ("name", "email", "product", "parent") # запретить редактировать


@admin.register(Status)
class StatusAdmin(TranslationAdmin):
    list_display = ("id", "name", "is_active", "created", "updated")
    list_display_links = ("name",)


@admin.register(Availability)
class AvailabilityAdmin(TranslationAdmin):
    list_display = ("id", "name", "is_active", "created", "updated")
    list_display_links = ("name",)


@admin.register(ImageHome)
class ImageHomeAdmin(TranslationAdmin):
    list_display = ("id", "get_image", "title", "draft")
    list_display_links = ("title",)
    list_editable = ("draft",)

    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="auto">')

    get_image.short_description = "Миниатюра"


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ("id", "title", "get_image", "draft",)
    list_display_links = ("title",)
    list_editable = ("draft",)


    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="50" height="auto">')

    get_image.short_description = "Миниатюра"
    readonly_fields = ("get_image", )


admin.site.title = "Admin panel"
admin.site.site_header = "Admin panel"
