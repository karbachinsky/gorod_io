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
import gorod.models.hub
from gorod.models.donc import DONC

import comments

from likes.models import Like

from abc import ABCMeta, abstractproperty, abstractmethod
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

    @abstractproperty
    def content_type(self):
        """
            model content_type
        """
        pass

    @property
    def required_depending_model_filter(self):
        """
            Required filter for depending model query set
            For example skip removed comments or you can specify period here
        """
        return None

    @abstractmethod
    def depending_model_related_pk(self, depending_object):
        pass

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

        for depending_object in depending_model_qs:
            object_pk = self.depending_model_related_pk(depending_object)

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

    def depending_model_related_pk(self, depending_object):
        return depending_object.object_pk

    required_depending_model_filter = dict(
        is_removed=False,
        content_type__name='article',
        content_type__app_label='gorod'
    )

    donc_filter = dict(
        field_name='comment_cnt',
        content_type=content_type
    )


class ArticlePositiveLikesCounter(DONCCounterBase):
    """
        Positive likes counter for articles
    """
    depending_model = Like
    model = gorod.models.article.Article

    content_type = ContentType.objects.get_for_model(model)

    def depending_model_related_pk(self, depending_object):
        return depending_object.object_pk

    required_depending_model_filter = dict(
        content_type__name='article',
        content_type__app_label='gorod'
    )

    donc_filter = dict(
        field_name='positive_likes_cnt',
        content_type=content_type
    )


class ArticleNegativeLikesCounter(ArticlePositiveLikesCounter):
    """
        Negative likes counter for articles
    """
    from copy import deepcopy
    donc_filter = deepcopy(ArticlePositiveLikesCounter.donc_filter)
    donc_filter['field_name'] = 'negative_likes_cnt'


class HubQuestionAnswersCounter(DONCCounterBase):
    """
        Count number of answers for questions
    """
    depending_model = gorod.models.hub.HubAnswer
    model = gorod.models.hub.HubQuestion

    def depending_model_related_pk(self, depending_object):
        return depending_object.question.id

    content_type = ContentType.objects.get_for_model(model)

    required_depending_model_filter = dict(
        is_published=False,
    )

    donc_filter = dict(
        field_name='answer_cnt',
        content_type=content_type
    )


class GroupArticlesCounter(DONCCounterBase):
    """
        Number of articles in group
    """
    depending_model = gorod.models.article.Article
    model = gorod.models.article.ArticleRubric

    content_type = ContentType.objects.get_for_model(model)

    def depending_model_related_pk(self, depending_object):
        return depending_object.rubric.id

    donc_filter = dict(
        field_name='articles_cnt',
        content_type=content_type
    )
