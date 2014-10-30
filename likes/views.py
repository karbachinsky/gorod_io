# -*- coding: utf-8 -*-

"""
    Likes views.
    Author: I. Karbachinsky
"""

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import models, IntegrityError, DatabaseError
from django.utils.translation import ugettext as _

from django.core.exceptions import ObjectDoesNotExist, ValidationError

from gorod.utils.views.mixins import JSONResponseMixin
from likes.models import Like
from likes.forms import LikeForm


class AddView(JSONResponseMixin, TemplateView):
    """
        Add like
    """
    @method_decorator(login_required)
    def _post(self, request):
        data = request.POST.copy()
        ctype = data.get("content_type")
        object_pk = data.get("object_pk")
        user = request.user

        if ctype is None or object_pk is None:
            return self.json_form_error_context(_(u'Кажется, что-то пошло не так :('))
        try:
            model = models.get_model(*ctype.split(".", 1))
            target = model._default_manager.get(pk=object_pk)

            if hasattr(target, 'add_like_hook'):
                target.add_like_hook()

        except (TypeError, AttributeError, ObjectDoesNotExist, ValueError, ValidationError):
            return self.json_form_error_context(_(u'Кажется, этот материла нельзя полайкать :('))

        # Construct like form
        form = LikeForm(target, data=data)

        # Check security information
        if form.security_errors():
            # hacker ?
            return self.json_form_error_context(_(u'Кажется, что-то пошло не так. Ты хакер? :('))

        if not request.user.can_action('add-like'):
            return self.json_form_error_context(_(u'Вы не можете лайкать так часто. Попробуйте позже!'))

        if form.is_valid():
            like = form.get_comment_object()
            like.user = user
            try:
                like.save()
            except (DatabaseError, IntegrityError) as e:
                return self.json_form_error_context(_(u'Кажется, что-то пошло не так :('))

            if not user.is_superuser:
                user.make_action('add-like')

            return self.json_success_context()
        else:
            return self.json_error_context(form.errors.items())




