# -*- coding: utf-8 -*-

"""
    Like template tag. Adds like to page
"""

from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.inclusion_tag('likes/templatetags/like.html', takes_context=False)
def like(data_object):
    content_type = ContentType.objects.get_for_model(type(data_object))

    return {
        'object': data_object,
        'content_type': content_type,
    }

