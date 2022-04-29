from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from utils.main import disable_for_loaddata



class Status(models.Model):
    name = models.CharField("Имя", max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField("Активен", default=True)
    created = models.DateTimeField("Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обновлен", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True, default=None, on_delete=models.SET_NULL)
    status = models.ForeignKey(Status, verbose_name="Статус", blank=True, null=True, on_delete=models.SET_NULL)
    firstname = models.CharField("Имя", max_length=50, blank=True, null=True, default=None)
    lastname = models.CharField("Фамилия", max_length=50, blank=True, null=True, default=None)
    email = models.EmailField("Email", blank=True, null=True, default=None)
    phone = models.CharField("Телефон", max_length=17, blank=True, null=True, default=None)
    city = models.CharField("Город", max_length=50, blank=True, null=True, default=None)
    created = models.DateTimeField("Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обновлен", auto_now_add=False, auto_now=True)
    total_price = models.FloatField("Сумма заказа", default=0)  # total price for all products in order

    def __str__(self):
        return f"№:{self.id}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, verbose_name="Заказ", blank=True, null=True, default=None, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name="Товар", blank=True, null=True, default=None, on_delete=models.SET_NULL)
    nmb = models.IntegerField("Количество", default=1)
    price_per_item = models.FloatField("Цена", default=0)
    total_price = models.FloatField("Сумма", default=0)  # price*nmb
    created = models.DateTimeField("Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обновлен", auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


    def save(self, *args, **kwargs):
        price_per_item = self.product.retail
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)



@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)



class ProductInBasket(models.Model):
    session_key = models.CharField("Ключ сессии", max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, verbose_name="Заказ", blank=True, null=True, default=None, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, verbose_name="Товар", blank=True, null=True, default=None, on_delete=models.CASCADE)
    nmb = models.IntegerField("Количество", default=0)
    price_per_item = models.FloatField("Цена за единицу", default=0)
    total_price = models.FloatField("Сумма заказа", default=0)#price*nmb
    created = models.DateTimeField("Создан", auto_now_add=True, auto_now=False)
    updated = models.DateTimeField("Обновлен", auto_now_add=False, auto_now=True)
    poster = models.ImageField("Изображение", blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


    def save(self, *args, **kwargs):
        self.price_per_item = self.product.retail
        self.total_price = int(self.nmb) * self.product.retail

        super(ProductInBasket, self).save(*args, **kwargs)

    @property
    def total_price_eur(self):
        price = self.product.retail_eur * self.nmb
        return round(price, 2)
    
    @property
    def total_price_usd(self):
        price = self.product.retail_usd * self.nmb
        return round(price, 2)

    @property
    def total_price_uah(self):
        price = self.product.retail_uah * self.nmb
        return round(price, 2)