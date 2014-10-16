"""
    Classes & Utilities that allow to count comments number for special
    gorod materials like article, question, etc.
"""
import comments
from abc import ABCMeta, abstractproperty, abstractmethod

from collections import Counter


class CommentCounterBase(object):

    Meta = ABCMeta

    @abstractproperty
    def comment_model(self):
        pass

    @abstractproperty
    def required_filter(self):
        pass



class ArticleCommentCounter(CommentCounterBase):
    comment_model = comments.get_model()

    required_filter = dict(
        is_removed_is=False
        content_type=  GET NECESSARY DJANGO CONTENT TYPE
    )

    def __init__(self):
        pass

    def recount(self):
        comments_qs = self.comment_model.objects.filter(**required_filter)

        data = Counter()

        for comment in comments_qs:
            object_pk = comment.object_pk

            data[object_pk] += 1


