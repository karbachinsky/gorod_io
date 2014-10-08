# -*- coding: utf-8 -*-

""" Template tags to work with strings """

from django import template
from django.utils.html import strip_tags, strip_entities

register = template.Library()


@register.filter(name='smart_truncate')
def smart_truncate(text, length_threshold):
    """
        Removes all values of arg from the given string
    """
    if not length_threshold:
        return text

    text = strip_tags(strip_entities(text))

    if len(text) <= length_threshold:
        return text

    if text[length_threshold-1] == u'.':
        return text[0:length_threshold]
    elif text[length_threshold-1] == u' ':
        return text[0:length_threshold-1] + u'...'
    else:
        return text[0:length_threshold] + u'...'
