from modeltranslation.translator import TranslationOptions, register
from .models import Product, Category, SubCategory, Status, Availability, News, ImageHome


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'material', 'country', 'packaging', 'description',)
    # fields = ('title', 'material', 'country', 'packaging', 'description', 'meta_title', 'meta_keywords', 'seo_text', 'meta_description', 'meta_og_title', 'meta_og_description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Status)
class StatusTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Availability)
class AvailabilityTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(ImageHome)
class ImageHomeTranslationOptions(TranslationOptions):
    fields = ('title', 'up_title', 'btn_name',)
