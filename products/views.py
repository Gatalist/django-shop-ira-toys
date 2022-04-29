from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_product.settings import product_in_page, new_product_data, id_product_new
from django_product.settings import product_count_index, news_count_index
from django.urls import reverse
from .models import Product, ImageHome, News, Category, SubCategory
from .forms import ReviewForm
from .tasks import product_new_info
from .service import range_date
import datetime



class CategoryView(ListView):
    """Category list"""
    
    def get(self, request):
        category = Category.objects.all()
        context = {"category_list": category}
        return render(request, "product/category_list.html", context)


class SubCategoryView(ListView):
    """SubCategory list"""
    
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        sub_category = SubCategory.objects.filter(category=category)
        context = {"category": category, "sub_category_list": sub_category}
        return render(request, "product/sub_category_list.html", context)


class ProductView(ListView):
    """Список продуктов"""
    model = Product
    paginate_by = product_in_page
    template_name = "product/product_list.html"
    allow_empty = True
    context_object_name = 'product_list'

    def get_queryset(self):
        product = Product.objects.filter(draft=True, category__slug=self.kwargs['subcategory'])
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(slug=self.kwargs['category'])
        context["subcategory"] = SubCategory.objects.get(slug=self.kwargs['subcategory'])
        return context


class ProductDetailView(DetailView):
    """Полное описание продукта"""
    model = Product
    slug_field = "slug"
    template_name = "product/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(slug=self.kwargs['category'])
        context["subcategory"] = SubCategory.objects.get(slug=self.kwargs['subcategory'])
        return context


class ProductNewsView(ListView):
    """Список продуктов | вывод всех новинок"""
    model = Product
    paginate_by = product_in_page
    template_name = "product/new_product_list.html"
    #allow_empty = False
    context_object_name = 'product_list'

    def get_queryset(self):   
        new_date = range_date()
        return Product.objects.filter(draft=True, dateAdd__range=[new_date[0], new_date[1]])

    def get_context_data(self, **kwargs):
        new_date = range_date()
        context = super().get_context_data(**kwargs)
        context["date"] = 'за 14 дней'
        return context


class NewProductDay(ListView):
    """Список продуктов | вывод новинок по дате"""
    model = Product
    paginate_by = product_in_page
    template_name = "product/new_product_list.html"
    allow_empty = True
    context_object_name = 'product_list'
    
    def get_queryset(self):
        product = Product.objects.filter(draft=True, dateAdd=self.kwargs['date'])
        return product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = self.kwargs['date']
        return context


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

    def get(self, request):
        imagehome_list = ImageHome.objects.filter(draft=True).order_by('-id')
        all_product = Product.objects.filter(draft=True, status_id=id_product_new)
        product = all_product[:product_count_index]
        # print(request.session['valuta'])
        return render(request, "product/index.html", {"imagehome_list": imagehome_list, "last_products": product})


class NewsView(ListView):
    """Новости"""
    paginate_by = product_in_page
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

    paginate_by = product_in_page
    template_name = "product/product_search.html"

    def get_queryset(self):
        return Product.objects.filter(title__icontains=self.request.GET.get("q"), draft=True)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
    