# -*- coding: utf-8 -*-

from rest_framework import serializers

from gorod.utils.serializers.user import UserSerializer
from gorod.utils.serializers.comment import CommentSerializer


class ArticleRubricSerializer(serializers.Serializer):
    """
    ArticleRubric serializer for feed
    """
    name = serializers.CharField()
    title = serializers.CharField()
    url = serializers.URLField()
    color = serializers.CharField()
    #picture = serializers.CharField()


class ArticleFeedSerializer(serializers.Serializer):
    """
    Article serializer for feed
    """
    id = serializers.IntegerField()
    user = UserSerializer()
    title = serializers.CharField()
    text = serializers.CharField()
    comment_cnt = serializers.IntegerField()
    raiting = serializers.IntegerField()
    thumbnail = serializers.CharField()
    human_add_date = serializers.CharField()
    comments = CommentSerializer()
    rubric = ArticleRubricSerializer()
    url = serializers.CharField()