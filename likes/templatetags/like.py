# -*- coding: utf-8 -*-

"""
    Like template tag. Adds like to page
"""

from django import template
from django.contrib.contenttypes.models import ContentType

from likes.models import Like

register = template.Library()


@register.inclusion_tag('likes/templatetags/like.html', takes_context=False)
def like(data_object, user=None):
    content_type = ContentType.objects.get_for_model(type(data_object))

    if user and user.is_authenticated():
        was_already_liked = Like.objects.has_user_liked_material(user, data_object)
    else:
        was_already_liked = False

    # FIXME
    return {
        'was_already_liked': int(was_already_liked),
        'object': data_object,
        # FIXME: make dynamic app getting
        'content_type': "gorod.%s" % content_type,
    }

