from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product, ImageHome, News, Category, SubCategory
from .forms import ReviewForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_product.settings import product_ip_page, news_ip_page, new_product_data, id_product_new
import datetime
from django.urls import reverse

# from django.template import loader
# from django.http import HttpResponse, HttpResponseRedirect



def category(request):
    """Список категорий"""
    category = Category.objects.all()
    context = {"category_list": category}
    return render(request, "product/category_list.html", context)



def subCategory(request, slug):
    """Список под категорий"""
    print(slug)
    category = Category.objects.get(slug=slug)
    sub_category = SubCategory.objects.filter(category=category)
    context = {"category": category, "sub_category_list": sub_category}
    return render(request, "product/sub_category_list.html", context)



def product_list(request, category, subcategory):
    """Список продуктов"""
    category = Category.objects.get(slug=category)
    sub_category = SubCategory.objects.get(slug=subcategory)
    products = Product.objects.filter(category=sub_category, draft=True)
    number = products.count()
    print(number)

    paginator = Paginator(products, product_ip_page)  # 3 posts in each page
    page = request.GET.get('page')
    
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        product = paginator.page(paginator.num_pages)

    context = {"category": category, "sub_category": sub_category, "product_list": product, "page": page, "number":number}

    return render(request, "product/product_list.html", context)



def product_detail(request, category, subcategory, slug):
    """Детали продукта"""
    category = Category.objects.get(slug=category)
    sub_category = SubCategory.objects.get(slug=subcategory)
    product = Product.objects.get(slug=slug)

    context = {"category": category, "sub_category": sub_category, "product": product}

    return render(request, "product/product_detail.html", context)



# вывод всех новинок
class ProductNewsView(View):
    """Детали продукта"""

    def get(self, request):

        end = datetime.date.today()
        start = end + datetime.timedelta(days=-new_product_data)

        date_end = str(end).split('-')
        date_start = str(start).split('-')

        end_year = int(date_end[0])
        end_mounth = int(date_end[1])
        end_day = int(date_end[2])

        start_year = int(date_start[0])
        start_mounth = int(date_start[1])
        start_day = int(date_start[2])

        search_start = datetime.date(start_year, start_mounth, start_day)
        search_end = datetime.date(end_year, end_mounth, end_day)

        products = Product.objects.filter(draft=True, status_id=id_product_new, dateAdd__range=[search_start, search_end]).order_by('-id')

        number = products.count()

        paginator = Paginator(products, product_ip_page)  # 3 posts in each page
        page = request.GET.get('page')
        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            product = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            product = paginator.page(paginator.num_pages)
            return product

        context = { "product_list": product, "page": page, "number":number}

        return render(request, "product/new_product_list.html", context)


# вывод новинок по дате
def productNews(request, date):
    
    products = Product.objects.filter(draft=True, status_id=id_product_new, dateAdd=date).order_by('-id')
    number = products.count()

    paginator = Paginator(products, product_ip_page)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        product = paginator.page(paginator.num_pages)

    context = { "product_list": product, "date": date, "page": page, "number":number}
    
    return render(request, "product/new_product_list.html", context)



class BasketDetailView(View):
    """Корзина заказов"""

    def get(self, request):
        return render(request, "product/basket_detail.html")


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect( f"/category/{product.category.category.slug}/{product.category.slug}/{product.slug}")


class IndexView(ListView):
    """главная"""
    model = ImageHome
    queryset = ImageHome.objects.filter(draft=True).order_by('-id')
    template_name = "product/index.html"


class NewsView(ListView):
    """Новости"""
    paginate_by = news_ip_page

    model = News
    queryset = model.objects.filter(draft=True).order_by('-dateAdd')
    template_name = "product/news.html"


class NewsDetailView(View):
    """Детали Новости"""
    
    def get(self, request, slug):
        news = News.objects.get(slug=slug)
        return render(request, "product/news_detail.html", {"news": news})


class AboutView(View):
    """О нас"""

    def get(self, request):
        return render(request, "product/about.html")        


class Search(ListView):
    """Поиск товара"""

    paginate_by = product_ip_page
    template_name = "product/product_search.html"

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get("q"))
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
    