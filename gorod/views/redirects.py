from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponsePermanentRedirect, Http404
from django.core.urlresolvers import reverse, NoReverseMatch

from gorod.models import Article


class ArticleRedirectView(View):
    def dispatch(self, request, city_name, article_id):
        article = get_object_or_404(Article, pk=article_id)
        try:
            redirect_url = reverse('gorod:article', kwargs={
                'city_name': city_name,
                'rubric_name': article.rubric.name,
                'article_id': article_id
            })
            return HttpResponsePermanentRedirect(redirect_url)
        except NoReverseMatch:
            raise Http404('Bad article redirect url')


class OrganizationRedirectView(View):
    def dispatch(self, request, city_name, organization_id):
        try:
            redirect_url = reverse('gorod:organization', kwargs={
                'city_name': city_name,
                'organization_id': organization_id
            })
            return HttpResponsePermanentRedirect(redirect_url)
        except NoReverseMatch:
            raise Http404('Bad organization redirect url')

