# -*- coding: utf-8 -*- 

""" Group filters """

from django import template
from django.core.urlresolvers import reverse
from django.core.context_processors import request
from django.db.models import Count

from gorod.models import ArticleRubric


register = template.Library()


@register.inclusion_tag('gorod/templatetags/group_filters.html', takes_context=True)
def group_filters(context, rubric):
    """
        Display group filters menu
    """

    city = context['city']
    filters = []

    url_named_params = context['request'].resolver_match.kwargs

    for filter_name, filter_title in ArticleRubric.FILTERS:
        # Adding about (city info module)
        filters.append({
            'title': filter_title,
            'url_name': filter_name,
            'link': reverse('gorod:feed-rubric-filter', kwargs={
                'city_name': city.name,
                'rubric_name': rubric.name,
                'filter_name': filter_name
            }),
            'is_active': filter_name == url_named_params.get('filter_name')
        })

    return {'filters': filters}


