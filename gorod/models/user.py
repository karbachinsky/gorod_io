from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse, NoReverseMatch

from gorod.models.base import City

from django.conf import settings

from datetime import datetime, timedelta
from django.utils import timezone


class User(AbstractUser):
    """
        Custom User: adding city and other
        profile information to default Django User model.
    """
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    avatar = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_user'

    def get_absolute_url(self, city=None):
        try:
            return reverse('gorod:user', kwargs={
                'user_id': self.id,
                'city_name': self.city.name,
            })
        except NoReverseMatch:
            return '/'

    profile_url = property(get_absolute_url)

    def get_stat(self):
        """
            Get internal user stat (UserStat object)
        """
        userstat, is_created = UserStat.objects.get_or_create(user=self)
        return userstat

    def __unicode__(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return self.username

    def can_action(self, action):
        """
            Check if user can add article.
        """
        userstat = self.get_stat()

        # FIXME
        if action == 'add-article':
            return userstat.can_action_add_article()
        elif action == 'add-comment':
            return userstat.can_action_add_comment()

    def make_action(self, action):
        """
            Update statistics after some user actions
        """
        userstat = self.get_stat()

        # FIXME
        if action == 'add-article':
            userstat.make_action_add_article()
        if action == 'add-comment':
            userstat.make_action_add_comment()


class UserStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article_last_add_time = models.DateTimeField(null=True)
    article_add_in_last_hour_cnt = models.SmallIntegerField(default=0)
    comment_last_add_time = models.DateTimeField(null=True)
    comment_add_in_last_hour_cnt = models.SmallIntegerField(default=0)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_userstat'

    def _article_last_add_was_more_then_hour_ago(self):
        if not self.article_last_add_time or\
                self.article_last_add_time < timezone.now() - timedelta(hours=1):
            return True
        return False

    def make_action_add_article(self):
        """
            Called when user adds article
        """
        if self._article_last_add_was_more_then_hour_ago():
            self.article_add_in_last_hour_cnt = 1
            self.article_last_add_time = timezone.now()
        else:
            self.article_add_in_last_hour_cnt += 1

        self.save()

    def can_action_add_article(self):
        """
            Checks if user can add article now
        """
        if self._article_last_add_was_more_then_hour_ago():
            return True
        if self.article_add_in_last_hour_cnt < settings.GOROD_ARTICLE_MAX_ADD_IN_HOUR_CNT:
            return True

        return False

    def _comment_last_add_was_more_then_hour_ago(self):
        if not self.comment_last_add_time or\
                self.comment_last_add_time < timezone.now() - timedelta(hours=1):
            return True
        return False

    def make_action_add_comment(self):
        """
            Called when user adds comment
        """
        if self._comment_last_add_was_more_then_hour_ago():
            self.comment_add_in_last_hour_cnt = 1
            self.comment_last_add_time = timezone.now()
        else:
            self.comment_add_in_last_hour_cnt += 1

        self.save()

    def can_action_add_comment(self):
        """
            Checks if user can add comment now
        """
        if self._comment_last_add_was_more_then_hour_ago():
            return True
        if self.comment_add_in_last_hour_cnt < settings.GOROD_COMMENT_MAX_ADD_IN_HOUR_CNT:
            return True

        return False