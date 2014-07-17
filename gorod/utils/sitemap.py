"""
    Sitemap.xml generator.
"""

from django.contrib.sitemaps import Sitemap
from gorod.models import Article, Organization


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


sitemaps = {
    'articles': ArticleSitemap(),
    'organizations': OrganizationSitemap()
}