# -*- coding: utf-8 -*- 

from django.shortcuts import get_object_or_404
#from django.core.context_processors import csrf

from gorod.models import City, ArticleRubric

 
def base_params(request):
    """ Construcing common context parameters """
    current_url_name = request.resolver_match.url_name
    current_url_params = request.resolver_match.kwargs

    context = {
        'current_url_name': current_url_name,
        #'csrf': csrf(request),
    }
    #assert False, csrf(request)

    if not current_url_params:
        return context

    if current_url_params.get('city_name'):
        context['city_name'] = current_url_params['city_name']           
        context['city'] = get_object_or_404(City, name=current_url_params['city_name'])
        context['rubrics'] = ArticleRubric.objects.select_related('donc_data').filter(city=context['city']).all()

    if current_url_params.get('rubric'):
        context['article_rubric'] = current_url_params['article_rubric']           

    if request.user.is_authenticated():
        context['notifications'] = request.user.get_last_notifications()

    return context

