"""
    Sitemap.xml generator.
"""

from django.contrib.sitemaps import Sitemap, GenericSitemap
from gorod.models import Article

articles_info = {
    'queryset': Article.objects.get_all_published(),
    'date_field': 'add_date'
}


sitemaps = {
    'articles': GenericSitemap(articles_info, priority=0.9, changefreq='monthly')
}

"""
class ArticleSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    def items(self):
        return Article.objects.get_all_published()

    def lastmode(self, obj):
        return obj.add_date

"""
