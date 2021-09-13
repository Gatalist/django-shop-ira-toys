from django.urls import path, re_path, register_converter
from django.conf.urls import url
from . import views

from . import path_converter

# register_converter(path_converter.DateConverter, 'yyyy')


# app_name = 'products'

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about-us/", views.AboutView.as_view(), name="about"),
    
    path("basket/", views.BasketDetailView.as_view(), name="basket_detail"),
    
    path("news/", views.NewsView.as_view(), name="news"),
    path("news/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("search/", views.Search.as_view(), name="search"),

    path("category/", views.category, name="category_list"),
    path("category/<slug:slug>/", views.subCategory, name="sub_category_list"),
    path("category/<slug:category>/<slug:subcategory>/", views.product_list, name="product_list"),
    path("category/<slug:category>/<slug:subcategory>/<slug:slug>/", views.product_detail, name="product_detail"),

    path('new_product/', views.ProductNewsView.as_view(), name="new_product_list"),
    path('new_product/<slug:date>/', views.productNews, name="new_product"),

    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]
