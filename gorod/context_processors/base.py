# -*- coding: utf-8 -*- 

from django.core.context_processors import request
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import AuthenticationForm

from gorod.models import City, ArticleRubric

 
def base_params(request):
    """ Construcing common context parameters """
    current_url_name = request.resolver_match.url_name
    current_url_params = request.resolver_match.kwargs

    context = {
        'current_url_name': current_url_name    
    }

    if not current_url_params:
        return context

    if current_url_params.get('city_name'):
        context['city_name'] = current_url_params['city_name']           
        context['city'] = get_object_or_404(City, name=current_url_params['city_name'])
        context['rubrics'] = ArticleRubric.objects.filter(city=context['city']).all()

    if current_url_params.get('rubric'):
        context['article_rubric'] = current_url_params['article_rubric']           

    return context

