# -*- coding: utf-8 -*-

"""
    Comments views.
    Author: I. Karbachinsky
"""

from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db import models, IntegrityError, DatabaseError
from django.utils.translation import ugettext as _

from django.core.exceptions import ObjectDoesNotExist, ValidationError

from gorod.utils.views.mixins import JSONResponseMixin

import comments


class AddView(JSONResponseMixin, TemplateView):
    """
        Post comment
    """
    def _get(self, *args, **kwargs):
        return self.json_forbidden_context(_(u'Ошибка!'))

    @method_decorator(login_required)
    def _post(self, request):
        data = request.POST.copy()
        ctype = data.get("content_type")
        object_pk = data.get("object_pk")
        user = request.user

        # FIXME: spike!
        data["name"] = user.username
        data["email"] = user.email

        if ctype is None or object_pk is None:
            return self.json_form_error_context(_(u'Кажется, что-то пошло не так :('))
        try:
            model = models.get_model(*ctype.split(".", 1))
            target = model._default_manager.get(pk=object_pk)
        except (TypeError, AttributeError, ObjectDoesNotExist, ValueError, ValidationError):
            return self.json_form_error_context(_(u'Кажется, для этого материала нельзя добавлять комментарии :('))

        # Construct the comment form
        form = comments.get_form()(target, data=data)

        # Check security information
        if form.security_errors():
            # hacker ?
            return self.json_form_error_context(_(u'Кажется, что-то пошло не так. Ты хакер? :('))

        if not request.user.can_action('add-comment'):
            return self.json_form_error_context(_(u'Вы не можете добавлять новые комментарии так часто. Попробуйте позже!'))

        if form.is_valid():
            comment = form.get_comment_object()
            comment.user = user
            try:
                comment.save()
            except (DatabaseError, IntegrityError) as e:
                return self.json_form_error_context(_(u'Кажется, что-то пошло не так :('))

            if not user.is_superuser:
                user.make_action('add-comment')

            return self.json_success_context()
        else:
            #assert False, form.errors
            return self.json_error_context(form.errors.items())




