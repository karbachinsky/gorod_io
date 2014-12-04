# -*- coding: utf-8 -*-


from rest_framework import serializers

from gorod.utils.serializers.user import UserSerializer
from gorod.utils.serializers.comment import CommentSerializer

from likes.models import Like


class ArticleRubricSerializer(serializers.Serializer):
    """
    ArticleRubric serializer for feed
    """
    name = serializers.CharField()
    title = serializers.CharField()
    url = serializers.CharField()
    color = serializers.CharField()


class ArticleFeedSerializer(serializers.Serializer):
    """
    Article serializer for feed
    """
    id = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()
    comment_cnt = serializers.IntegerField()
    raiting = serializers.IntegerField()
    thumbnail = serializers.CharField()
    human_add_date = serializers.CharField()
    comments = CommentSerializer()
    user = UserSerializer()
    rubric = ArticleRubricSerializer()
    url = serializers.CharField()

    def __init__(self, *args, **kwargs):
        self.was_already_liked = True
        super(ArticleFeedSerializer, self).__init__(*args, **kwargs)

