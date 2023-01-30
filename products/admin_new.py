from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
from modeltranslation.admin import TranslationAdmin
from tabbed_admin import TabbedModelAdmin
from django.db import models
from django.forms import TextInput, Textarea
from .models import Category, Product, Reviews, ProductImage, ImageHome, News, Status, SubCategory, Availability


class ProductAdminForm(forms.ModelForm):
    # description_ru = forms.CharField(label='Описание [ru]', widget=CKEditorUploadingWidget())
    # description_uk = forms.CharField(label='Описание [uk]', widget=CKEditorUploadingWidget())
    description_ru = forms.Textarea()
    description_uk = forms.Textarea()

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "get_image", "updated")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="50" height="auto">')

    get_image.short_description = "Изображение"
    readonly_fields = ("get_image", )

    fieldsets = (
        ("", {
            "fields": (("name_ru",), ("name_uk",),)
        }),
        ("", {
            "fields": (("slug",),)
        }),
        ("", {
            "fields": (("poster", "get_image",),)
        }),
        ("", {
            "fields": (("alt",),)
        }),
    )

    # def has_add_permission(self, request):
    #     return False


@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    list_display = ("id", "name", "get_image", "updated")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="50" height="auto">')

    get_image.short_description = "Изображение"
    readonly_fields = ("get_image", )

    fieldsets = (
        ("", {
            "fields": (("category",),)
        }),
        ("", {
            "fields": (("name_ru",), ("name_uk",),)
        }),
        ("", {
            "fields": (("slug",),)
        }),
        ("", {
            "fields": (("poster", "get_image",),)
        }),
        ("", {
            "fields": (("alt",),)
        }),
    )


class ReviewInline(admin.StackedInline):
    model = Reviews
    extra = 1

    fieldsets = (
        ("", {
            "fields": (("name",), ("email",),)
        }),
        ("", {
            "fields": (("dateAdd",),)
        }),
        ("", {
            "fields": (("text",),)
        }),
    )


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="auto">')


    get_image.short_description = "загружено"

    fieldsets = (
        ("", {
            "fields": (("get_image",),)
        }),
        ("", {
            "fields": (("image", "alt",),)
        }),
    )


@admin.register(Product)
class ProductAdmin(TabbedModelAdmin, TranslationAdmin):
    list_display = ("id", "title", "get_image", "category", "dateAdd", "updated", "draft")
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

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':100})},
    }

    tab_fields_1 = (
        ("", {
            "fields": (("draft",),),
        }),
        ("", {
            "fields": (("dateAdd"),)
        }),
        ("", {
            "fields": (("retail"),)
        }),
        ("", {
            "fields": (("status",),)
        }),
        ("", {
            "fields": (("category"),)
        }),
        ("", {
            "fields": (("availability",),)
        }),
        ("", {
            "fields": (("article",),)
        }),
        ("", {
            "fields": (("title_ru", "title_uk",),)
        }),
        ("", {
            "fields": (("slug",),)
        }),
    )

    tab_fields_2 = (     
        ("", {
            "fields": (("material_ru", "material_uk",),)
        }),
        ("", {
            "fields": (("country_ru", "country_uk",),)
        }),
        ("", {
            "fields": (("packaging_ru", "packaging_uk",),)
        }),
        ("", {
            "fields": (("size",),)
        }),  
    )
    
    tab_fields_3 = (
        ("", {
            "fields": (("description_ru",), ("description_uk",),)
        }),
    )

    tab_image = (
        ("Главное изображение", {
            "fields": (("poster", "get_image", "alt",),)
        }),
        ProductImageInline,
    )

    tab_seo = (
        ("", {
            "fields": (("noindex", "nofollow",),)
        }),
        ("", {
            "fields": (("canonical",),)
        }),
        ("title", {
            "fields": (("meta_title_ru",), ("meta_title_uk",),),
        }),
        ("keywords", {
            "fields": (("meta_keywords_ru",), ("meta_keywords_uk",),)
        }),
        ("description", {
            "fields": (("meta_description_ru",), ("meta_description_uk",),)
        }),
        ("og:title", {
            # "description": ("Description for the fieldset"),
            "fields": (("meta_og_title_ru",), ("meta_og_title_uk",),)
        }),
        ("og:description", {
            "fields": (("meta_og_description_ru",), ("meta_og_description_uk",),)
        }),
        ("SEO text", {
            "fields": (("seo_text_ru",), ("seo_text_uk",),)
        }),
    )

    tab_review = (
        ReviewInline,
    )

    tabs = [
        ('Основное', tab_fields_1),
        ('Характеристики', tab_fields_2),
        ('Описание', tab_fields_3),
        ('Изображение', tab_image),
        ('SEO', tab_seo),
        ('Отзывы', tab_review),
    ]
    
    # inlines = [ProductImageInline, ReviewInline, ]

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


# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     list_display = ("id", "alt", "get_image", "product",)
#     list_display_links = ("alt",)
#     readonly_fields = ("get_image", )

#     def get_image(self, obj):
#         return mark_safe(f'<img src="{obj.image.url}" width="50" height="auto">')

#     get_image.short_description = "Изображение"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "text",) # порядок отображения
    list_display_links = ("name", "text",) # ссылка
    readonly_fields = ("name", "email", "product", "parent", "dateAdd",) # запретить редактировать

    fieldsets = (
        ("", {
            "fields": (("name",), ("email",), ("product",))
        }),
        ("", {
            "fields": (("dateAdd",),)
        }),
        ("", {
            "fields": (("text",),)
        }),
    )


@admin.register(Status)
class StatusAdmin(TranslationAdmin):
    list_display = ("id", "name", "is_active", "created", "updated")
    list_display_links = ("name",)

    fieldsets = (
        ("", {
            "fields": (("is_active",),)
        }),
        ("", {
            "fields": (("name_ru",), ("name_uk",),)
        }),
    )


@admin.register(Availability)
class AvailabilityAdmin(TranslationAdmin):
    list_display = ("id", "name", "is_active", "created", "updated")
    list_display_links = ("name",)

    fieldsets = (
        ("", {
            "fields": (("is_active",),)
        }),
        ("", {
            "fields": (("name_ru",), ("name_uk",),)
        }),
    )


@admin.register(ImageHome)
class ImageHomeAdmin(TabbedModelAdmin, TranslationAdmin):
    list_display = ("id", "get_image", "title", "draft")
    list_display_links = ("title", "get_image")
    list_editable = ("draft",)

    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="auto">')

    get_image.short_description = "Изображение"

    tab_basic = (
        ("", {
            "fields": (("draft",),)
        }),
        ("", {
            "fields": (("status",),)
        }),
        ("", {
            "fields": (("title_ru",), ("title_uk",),)
        }),
        ("", {
            "fields": (("up_title_ru",), ("up_title_uk",),)
        }),
    )

    tab_image = (
        ("", {
            "fields": (("image", "get_image",),)
        }),
        ("", {
            "fields": (("alt",),)
        }),
    )

    tab_button = (
        ("Если текста не будет, кнопка не будет отображаться", {
            "fields": (("btn_name_ru",), ("btn_name_uk",),)
        }),
        ("Ниже можно выбрать один из 3 вариантов ссылки, все заполнять не нужно!", {
            "fields": ()
        }),
        ("Ссылка на страницу", {
            "fields": (("slug",),)
        }),
        ("Или ссылка на товар", {
            "fields": (("product",),)
        }),
        ("Или ссылка на новость", {
            "fields": (("product",),)
        }),
    )

    tabs = [
        ('Основное', tab_basic),
        ('Изображение', tab_image),
        ('Кнопка', tab_button),
    ]


@admin.register(News)
class NewsAdmin(TabbedModelAdmin, TranslationAdmin):
    list_display = ("id", "title", "get_image", "draft",)
    list_display_links = ("title",)
    list_editable = ("draft",)


    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="50" height="auto">')

    get_image.short_description = "Миниатюра"
    readonly_fields = ("get_image", )

    basic = (
        ("", {
            "fields": (("draft",),)
        }),
        ("", {
            "fields": (("dateAdd",),)
        }),
        ("", {
            "fields": (("title_ru", "title_uk",),)
        }),
        ("", {
            "fields": (("slug",),)
        }),
        ("Изображение", {
            "fields": (("get_image", "poster", "alt",),)
        }),
    )

    description = (
        ("", {
            "fields": (("description_ru", "description_uk",),)
        }),
    )

    tabs = [
        ('Основное', basic),
        ('Описание', description),
    ]


admin.site.title = "Admin panel"
admin.site.site_header = "Admin panel"
