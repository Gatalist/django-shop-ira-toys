from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.base import View
from django.utils import translation
from django_product.settings import product_in_page, product_count_index
from .models import Product, ImageHome, News, Category, SubCategory
from .forms import ReviewForm
from .service import range_date
from .mixin import MixinMetaTags


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
        product = Product.objects.filter(draft=True, category__slug=self.kwargs['subcategory']).select_related('category', 'availability', 'status')
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
    context_object_name = 'product_list'

    def get_queryset(self):
        new_date = range_date()
        return Product.objects.filter(draft=True, dateAdd__range=[new_date[0], new_date[1]]).select_related('category', 'availability', 'status')

    def get_context_data(self, **kwargs):
        lang = translation.get_language()
        context = super().get_context_data(**kwargs)
        if lang == 'ru':
            context["date"] = 'за 14 дней'
        elif lang == 'uk':
            context["date"] = 'за 14 днів'
        return context


class NewProductDay(ListView):
    """Список продуктов | вывод новинок по дате"""
    model = Product
    paginate_by = product_in_page
    template_name = "product/new_product_list.html"
    allow_empty = True
    context_object_name = 'product_list'

    def get_queryset(self):
        product = Product.objects.filter(draft=True, dateAdd=self.kwargs['date']).select_related('category', 'availability', 'status')
        return product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = self.kwargs['date']
        return context


class BasketDetailView(TemplateView):
    """Корзина заказов"""
    template_name = "product/basket_detail.html"


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
        
        return redirect(product)


class IndexView(MixinMetaTags, ListView):
    """главная"""
    model = Product
    template_name = "product/index.html"
    context_object_name = 'last_products'

    def get_queryset(self):
        return Product.objects.filter(draft=True)[:product_count_index].select_related('category', 'availability', 'status')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["meta_tags"] = self.meta_tags
        context["imagehome_list"] = ImageHome.objects.filter(draft=True).order_by('-id').select_related('product', 'news', 'status')
        return context


class NewsView(ListView):
    """Новости"""
    paginate_by = product_in_page
    model = News
    queryset = model.objects.filter(draft=True).order_by('-dateAdd')
    template_name = "product/news.html"


class NewsDetailView(DetailView):
    """Детали Новости"""
    model = News
    template_name = "product/news_detail.html"


class AboutView(TemplateView):
    """О нас"""
    template_name = "product/about.html"


class Search(ListView):
    """Поиск товара"""
    paginate_by = product_in_page
    template_name = "product/product_search.html"

    def get_queryset(self):
        try:
            if int(self.request.GET.get("q")):
                return Product.objects.filter(id=self.request.GET.get("q"), draft=True)
        except:
            if not self.request.GET.get("q"):
                return Product.objects.filter(draft=True)
            else:
                return Product.objects.filter(title__icontains=self.request.GET.get("q"), draft=True)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        if not self.request.GET.get("q"):
            context["q_name"] = ''
        else:
            context["q_name"] = self.request.GET.get("q")
        return context
