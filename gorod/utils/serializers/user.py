# -*- coding: utf-8 -*-

#from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """
    User model serializer
    """
    profile_url = serializers.CharField()
    human_name = serializers.CharField()
    full_avatar = serializers.CharField()