"""
    Sitemap.xml generator.
"""

from django.contrib.sitemaps import Sitemap, GenericSitemap
from gorod.models import Article, Organization, CityWelcome, CityInfoQuestion

articles_info = {
    'queryset': Article.objects.get_all_published(),
    'date_field': 'add_date'
}

organizations_info = {
    'queryset': Organization.objects.get_all_published(),
    'date_field': 'add_date'
}

citywelcomes_info = {
    'queryset': CityWelcome.objects.all(),
    'date_field': 'add_date'
}

cityinfo_questions_info = {
    'queryset': CityInfoQuestion.objects.all().select_related(),
    'date_field': 'add_date'
}

sitemaps = {
    'articles': GenericSitemap(articles_info, priority=0.9, changefreq='monthly'),
    'organizations': GenericSitemap(organizations_info, priority=0.9, changefreq='weekly'),
    'citywelcomes': GenericSitemap(citywelcomes_info, priority=0.5, changefreq='monthly'),
    'cityinfo_questions': GenericSitemap(cityinfo_questions_info, priority=0.5, changefreq='monthly')
}

"""
class ArticleSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    def items(self):
        return Article.objects.get_all_published()

    def lastmode(self, obj):
        return obj.add_date


class OrganizationSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Organization.objects.get_all_published()

    def lastmode(self, obj):
        return obj.add_date
"""
