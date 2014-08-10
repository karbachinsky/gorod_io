# -*- coding: utf-8 -*- 

"""
    User template tag.
    Renders user avatar and first/last name representaion
    Author: I. Karbachinsky
"""

from django import template
from django.core.urlresolvers import reverse
from django.core.context_processors import request
from django.db.models import Count

from gorod.models import ArticleRubric, Article


register = template.Library()


@register.inclusion_tag('gorod/templatetags/user.html', takes_context=True)
def user(context, user):
    """ Basic user representation in frontend pages """
    return {'user': user}


