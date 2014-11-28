# -*- coding: utf-8 -*-

from rest_framework import serializers

from gorod.utils.serializers.user import UserSerializer


class CommentSerializer(serializers.Serializer):
    """
    Comment model serializer
    """
    user = UserSerializer()
    comment = serializers.CharField()
    submit_date = serializers.CharField()
