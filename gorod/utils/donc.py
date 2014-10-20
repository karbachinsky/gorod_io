"""
    DONC = Depending objects number counter.
    This Classes & Utilities allow to count number of various depending objects for
    certain gorod objects.
    Example:
        - Article and number of it's comments
        - Question and number of it's answers.
    We can't always join tables on each user request to get necessary number
    because it's too expensive and slow. So, we do it periodically
    at background by some fixed portions.

    Author: I. Karbachinsky <igorkarbachinsky@mail.ru>
"""
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError

from gorod.utils.exceptions import DONCError
import gorod.models.article
from gorod.models.donc import DONC
import comments

from abc import ABCMeta, abstractproperty
from collections import Counter


class DONCCounterBase(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def model(self):
        """
            Model for whom we count number of something.
        """
        pass

    @abstractproperty
    def depending_model(self):
        """
            Model, which number we are recounting
        """
        pass

    @abstractproperty
    def donc_filter(self):
        """
            filter to get necessary donc for object
        """
        pass

    @property
    def required_depending_model_filter(self):
        """
            Required filter for depending model query set
            For example skip removed comments or you can specify period here
        """
        return None

    def __init__(self):
        pass

    def recount(self, object_id):
        depending_model_qs = self.depending_model.objects.all()
        if self.required_depending_model_filter:
            depending_model_qs.filter(**self.required_depending_model_filter)
            if object_id:
                depending_model_qs.filter(
                    object_pk=object_id
                )

        data = Counter()

        for comment in depending_model_qs:
            object_pk = comment.object_pk

            if not object_pk in data:
                data[object_pk] = 1
            else:
                data[object_pk] += 1

        for object_pk, cnt in data.iteritems():
            self.set_object_cnt(object_pk, cnt)

    def set_object_cnt(self, object_pk, cnt):
        try:
            object_donc, _ = DONC.objects.get_or_create(
                object_pk=object_pk,
                **self.donc_filter
            )

            object_donc.count = cnt
            object_donc.save()
        except IntegrityError as e:
            raise DONCError(e)


class ArticleCommentsCounter(DONCCounterBase):
    """
        Count number of comments for articles
    """
    depending_model = comments.get_model()
    model = gorod.models.article.Article

    content_type = ContentType.objects.get_for_model(model)

    required_depending_model_filter = dict(
        is_removed=False,
        content_type__name='article',
        content_type__app_label='gorod'
    )

    donc_filter = dict(
        field_name='comment_cnt',
        content_type=content_type
    )


