# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse
# from products.models import Product, Category, SubCategory, News


# class StaticSitemap(Sitemap):
#     changefreq = "monthly"
#     priority = 0.8
#     protocol = 'https'

#     def items(self):
#         return ['/', '/about-us/', '/news/', '/basket/', '/new_product/']

#     def location(self, item):
#         return item


# class ProductSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.6
#     protocol = 'https'

#     def items(self):
#         return Product.objects.filter(draft=True)

#     def lastmod(self, obj):
#         return obj.updated
        
#     def location(self,obj):
#         return obj.get_absolute_url()


# class CategorySitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.6
#     protocol = 'https'

#     def items(self):
#         return Category.objects.all()

#     def lastmod(self, obj):
#         return obj.updated
        
#     def location(self,obj):
#         return obj.get_absolute_url()


# class SubCategorySitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.6
#     protocol = 'https'

#     def items(self):
#         return SubCategory.objects.all()

#     def lastmod(self, obj):
#         return obj.updated
        
#     def location(self,obj):
#         return obj.get_absolute_url()


# class NewsSitemap(Sitemap):
#     changefreq = "weekly"
#     priority = 0.6
#     protocol = 'https'

#     def items(self):
#         return News.objects.filter(draft=True)

#     def lastmod(self, obj):
#         return obj.updated
        
#     def location(self,obj):
#         return obj.get_absolute_url()