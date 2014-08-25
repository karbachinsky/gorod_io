# -*- coding: utf-8 -*- 

""" Menu template tags for gorod """ 

from django import template
from django.core.urlresolvers import reverse
from django.core.context_processors import request
from django.db.models import Count

from gorod.models import ArticleRubric, Article


register = template.Library()


@register.inclusion_tag('gorod/templatetags/menu.html', takes_context=True)
def menu(context, city):
    """ Display menu for city """

    request = context['request']

    current_url_name = request.resolver_match.url_name 
    url_named_params = request.resolver_match.kwargs;

    menu = []

    if url_named_params.get('rubric_name'):
        current_url_name += '_' + url_named_params['rubric_name']

    # Adding organizations
    menu.append({
        'title': 'Организации',
        'url_name': 'organizations',
        'link': reverse('gorod:organizations', kwargs={'city_name': city.name}),
        'is_active': 0
    })

    # Adding about (city info module)
    menu.append({
        'title': 'Вопросы и ответы',
        'url_name': 'hub',
        'link': reverse('gorod:hub', kwargs={'city_name': city.name}),
        'is_active': 0
    })

    # Setting active
    for menuitem in menu:
        if menuitem['url_name'] == current_url_name:
            menuitem['is_active'] = 1
            break

    return {'menu': menu}


