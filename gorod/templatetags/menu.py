# -*- coding: utf-8 -*- 

""" Menu template tags for gorod """ 

from django import template
from django.core.urlresolvers import reverse
from django.core.context_processors import request
from django.db.models import Count

from gorod.models import ArticleRubric, Article


register = template.Library()


@register.inclusion_tag('gorod/templatetags/menu.html', takes_context = True)
def menu(context, city):
    """ Display menu for city """

    request = context['request']

    #raise Exception({request.resolver_match}) 

    current_url_name = request.resolver_match.url_name 
    url_named_params = request.resolver_match.kwargs;

    # First element is city
    menu = [{
        'title': city.title,
        'url_name': 'city_main_page',
        'link': reverse('gorod:city_main_page', kwargs={ 'city_name': city.name }),
        'is_active': 0
    }]

    if url_named_params.get('rubric_name'):
        current_url_name += '_' + url_named_params['rubric_name']

    # Than addding list of rubrics
    # Getting rubrics where there are al least one active article
    # FIXME: cache and add to context processors
    #active_rubrics = ArticleRubric.objects.annotate(Count('authors'))
    active_rubrics = Article.objects.filter(city=city.id).values('rubric__name','rubric__title').distinct().all()
    
    #raise Exception(active_rubrics)

    for rubric in list(active_rubrics):
        menuitem = {
            'title': rubric['rubric__title'],
            'url_name': 'feed_rubric_' + rubric['rubric__name'],
            'link': reverse('gorod:feed_rubric', kwargs={ 
                'city_name': city.name, 
                'rubric_name': rubric['rubric__name']
            }),
            'is_active': 0
        }

        menu.append(menuitem)

    # Adding organizations
    menu.append({
        'title': 'Организации',
        'url_name': 'organizations',
        'link': reverse('gorod:organizations', kwargs={'city_name': city.name}),
        'is_active': 0
    })

    # Setting active
    for menuitem in menu:
        if menuitem['url_name'] == current_url_name:
            menuitem['is_active'] = 1
            break


    return {'menu': menu}


