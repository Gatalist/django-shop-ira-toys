# from django.views.decorators.cache import cache_page
from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    
    path("about-us/", views.AboutView.as_view(), name="about"),
    
    path("basket/", views.BasketDetailView.as_view(), name="basket_detail"),
    
    path("news/", views.NewsView.as_view(), name="news"),
    path("news/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    
    path("search/", views.Search.as_view(), name="search"),

    path("category/", views.CategoryView.as_view(), name="category_list"),
    path("category/<slug:slug>/", views.SubCategoryView.as_view(), name="sub_category_list"),
    path("category/<slug:category>/<slug:subcategory>/", views.ProductView.as_view(), name="product_list"),
    path("category/<slug:category>/<slug:subcategory>/<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),

    path('new_product/', views.ProductNewsView.as_view(), name="new_product_list"),

    path('new_product/<slug:date>/', views.NewProductDay.as_view(), name="new_product"),

    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
]
