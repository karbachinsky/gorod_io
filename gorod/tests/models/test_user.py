"""
    User model test
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings

from datetime import datetime
from django.utils import timezone


class UserTestCase(TestCase):
    """
        Test User model methods
    """

    def setUp(self):
        self.user = get_user_model()()
        self.user.save()

    def test_can_action_add_article(self):
        """ """
        # Creating user
        user = self.user

        self.assertTrue(user.can_action('add-article'), "New user must be able to add articles!")

        userstat = user.get_stat()

        userstat.article_last_add_time = timezone.now()
        userstat.save()

        self.assertTrue(user.can_action('add-article'), "user with zero added articles \
            must be able to add articles!")

        userstat.article_add_in_last_hour_cnt = settings.GOROD_ARTICLE_MAX_ADD_IN_HOUR_CNT - 1
        userstat.save()

        self.assertTrue(user.can_action('add-article'), "user still must be able to add articles!")

        userstat.article_add_in_last_hour_cnt = settings.GOROD_ARTICLE_MAX_ADD_IN_HOUR_CNT
        userstat.save()

        self.assertIs(user.can_action('add-article'), False, "user exceed his limit! He must not be able \
            to add new articles during next hour!")

    def test_make_action_add_article(self):
        """ """
        # Creating user
        user = self.user

        for i in xrange(settings.GOROD_ARTICLE_MAX_ADD_IN_HOUR_CNT-1):
            user.make_action('add-article')
            self.assertTrue(user.can_action('add-article'), "User still can add articles!")

        user.make_action('add-article')
        self.assertIs(user.can_action('add-article'), False, "User should exhaust his add article limit!")