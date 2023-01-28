from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from datetime import date
from django.urls import reverse
from currency.models import Usd


class Category(models.Model):
    """Категория"""
    name = models.CharField('Категория', max_length=150)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="url")
    poster = models.ImageField("Изображение", upload_to='category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        return reverse("sub_category_list", kwargs={"slug": self.slug})


class SubCategory(models.Model):
    """Категория"""
    name = models.CharField('Под Категория', max_length=150)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="url")
    category = models.ForeignKey(Category, verbose_name = "Категория", blank=True, null=True, on_delete=models.SET_NULL)
    poster = models.ImageField("Изображение", upload_to='sub-category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Под Категория"
        verbose_name_plural = "Под Категории"

    def get_absolute_url(self):
        return f"{self.slug}"
    
    def get_absolute_url_my(self):
        return reverse("product_list", kwargs={"category": self.category.category.slug, "subcategory": self.category.slug})


class Status(models.Model):
    name = models.CharField("Имя", max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField("Активен", default=True)
    created = models.DateTimeField("Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обновлен", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Availability(models.Model):
    name = models.CharField("Имя", max_length=25, blank=True, null=True, default=None)
    is_active = models.BooleanField("Активен", default=True)
    created = models.DateTimeField("Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обновлен", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Наличие'
        verbose_name_plural = 'Наличие'


class Product(models.Model):
    """Продукт"""
    draft = models.BooleanField("Включен", default=False)
    status = models.ForeignKey(Status, verbose_name="Статус", null=True, blank=True, on_delete=models.CASCADE)
    availability = models.ForeignKey(Availability, verbose_name="Наличие", default=1, on_delete=models.CASCADE)
    title = models.CharField("Название", max_length=250)
    article = models.CharField("Штрих-код", max_length=15, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="url")
    category = models.ForeignKey(SubCategory, verbose_name = "Категория", null=True, blank=True, on_delete=models.SET_NULL)
    dateAdd = models.DateField("Добавлен", default=date.today)
    material = models.CharField("Материал", null=True, blank=True, max_length=100)
    country = models.CharField("Страна", null=True, blank=True, max_length=150)
    packaging = models.CharField("Упаковка", null=True, blank=True, max_length=150)
    size = models.CharField("Размер", null=True, blank=True, max_length=150)
    retail = models.FloatField("Цена", null=True, help_text="")
    description = RichTextUploadingField("Описание", max_length=5000)
    poster = models.ImageField("Изображение", upload_to='products/')
    
    def __str__(self):
        return self.title

    def get_absolute_url_my(self):
        return reverse("product_detail", kwargs={"category": self.category.category.slug, "subcategory": self.category.slug, "slug": self.slug})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    @property
    def retail_uah(self):
        usd = Usd.objects.latest('id')
        result = usd.name * self.retail
        return round(result, 2)
    
    @property
    def retail_usd(self):
        return self.retail

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['availability', 'status', '-id']


class ProductImage(models.Model):
    "Изображения товара"
    title = models.CharField("Заголовок", max_length=150)
    image = models.ImageField("Изображение", upload_to='products_image/')
    product = models.ForeignKey(Product, verbose_name = "Продукт", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name =  "Изображение товара"
        verbose_name_plural =  "Изображение товаров"


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Отзыв', max_length=5000)
    dateAdd = models.DateField("Дата добавления", default=date.today)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )

    product = models.ForeignKey(Product, verbose_name = "Товар", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-id']


class News(models.Model):
    """Новости"""
    draft = models.BooleanField("Показывать на сайте", default=False)
    title = models.CharField("Название", max_length=250)
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="url")
    dateAdd = models.DateField("Дата добавления", default=date.today)
    description = RichTextUploadingField("Текст публикации")
    poster = models.ImageField("Изображение", upload_to='news/')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.slug})
  
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['-id']


class ImageHome(models.Model):
    """слайдер на главной"""
    draft = models.BooleanField("Показывать на сайте", default=True)
    status = models.ForeignKey(Status, verbose_name="Статус", null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField("Заголовок", null=True, blank=True, max_length=100)
    up_title = models.CharField("Подзаголовок", null=True, blank=True, max_length=50)
    product = models.ForeignKey(Product, verbose_name="Продукт", null=True, blank=True, on_delete=models.CASCADE)
    news = models.ForeignKey(News, verbose_name="Новость", null=True, blank=True, on_delete=models.CASCADE)
    slug = models.CharField("url", null=True, blank=True, max_length=250)
    btn_name = models.CharField("Текст на кнопке", null=True, blank=True, default='Подробнее', max_length=50)
    image = models.ImageField("Изображение", upload_to="image_home/")
    
    def __str__(self):
        return f'{self.product}'

    class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды на главной"
        ordering = ['-id']
