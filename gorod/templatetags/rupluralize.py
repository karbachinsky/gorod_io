# -*- coding: utf-8 -*-

from django.template import Library, TemplateSyntaxError
from django.template.defaultfilters import stringfilter
register = Library()

@register.filter
@stringfilter
def rupluralize(value, arg):
    bits = arg.split(u',')
    try:
        if str(value).endswith('1'):
            return bits[0]
        elif str(value)[-1:] in '234':
            return bits[1]
        else:
            return bits[2]
    except:
        raise TemplateSyntaxError
    return ''

rupluralize.is_safe = False

