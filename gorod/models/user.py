from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse, NoReverseMatch
from django.templatetags.static import static
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from gorod.models.base import City

from django.conf import settings

from datetime import timedelta
from django.utils import timezone


class Notification(models.Model):
    """
        User Notification
    """
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    ctime = models.DateTimeField(auto_now_add=True)
    # User who has made action to be notified
    target_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Content-object field on which was action
    content_type = models.ForeignKey(ContentType,
        verbose_name=_('content type'),
        related_name="content_type_set_for_%(class)s"
    )
    object_pk = models.PositiveIntegerField(_('object ID'))
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    action = models.CharField(max_length=100)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_notification'


class User(AbstractUser):
    """
        Custom User: adding city and other
        profile information to default Django User model.
    """
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    notifications = models.ManyToManyField('Notification')

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
        return self.human_name

    @property
    def human_name(self):
        if self.first_name and self.last_name:
            return "%s %s" % (self.first_name, self.last_name)
        return self.username

    def full_avatar(self):
        """
            If avatar is set then returning it. Else getting default avatar
        """
        return self.avatar or self._default_avatar

    def can_action(self, action):
        """
            Check if user can add article.
        """
        userstat = self.get_stat()

        if action.startswith('add-'):
            model_type = action.replace('add-', '')
            return userstat.can_timenumber_action(
                model_type=model_type,
                threshold=getattr(settings, "GOROD_%s_MAX_ADD_IN_HOUR_CNT" % model_type.upper())
            )

    def make_action(self, action):
        """
            Update statistics after some user actions
        """
        userstat = self.get_stat()

        if action.startswith('add-'):
            userstat.make_timenumber_action(action.replace('add-', ''))

    @property
    def _default_avatar(self):
        return static('gorod/img/userava.png')

    def add_notification(self, target, target_user, action):
        """
            Add notification to user
        """
        notification = Notification(
            target_user=target_user,
            action=action,
            object_pk=target.id,
            content_type=ContentType.objects.get_for_model(type(target))
        )
        notification.save()

        self.notifications.add(notification)


class UserStat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # FIXME
    article_last_add_time = models.DateTimeField(null=True)
    article_add_in_last_hour_cnt = models.SmallIntegerField(default=0)

    comment_last_add_time = models.DateTimeField(null=True)
    comment_add_in_last_hour_cnt = models.SmallIntegerField(default=0)

    hubanswer_last_add_time = models.DateTimeField(null=True)
    hubanswer_add_in_last_hour_cnt = models.SmallIntegerField(default=0)

    hubquestion_last_add_time = models.DateTimeField(null=True)
    hubquestion_add_in_last_hour_cnt = models.SmallIntegerField(default=0)

    like_last_add_time = models.DateTimeField(null=True)
    like_add_in_last_hour_cnt = models.SmallIntegerField(default=0)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_userstat'

    def _last_add_was_more_then_hour_ago(self, model_type):
        last_add_time = getattr(self, "%s_last_add_time" % model_type)
        if not last_add_time or last_add_time < timezone.now() - timedelta(hours=1):
            return True
        return False

    def make_timenumber_action(self, model_type):
        """
            When adding some material
        """
        last_add_time_attr_name = "%s_last_add_time" % model_type
        add_in_last_hour_cnt_attr_name = "%s_add_in_last_hour_cnt" % model_type

        last_add_time = getattr(self, last_add_time_attr_name)
        add_in_last_hour_cnt = getattr(self, add_in_last_hour_cnt_attr_name)

        if self._last_add_was_more_then_hour_ago(model_type):
            setattr(self, add_in_last_hour_cnt_attr_name, 1)
            setattr(self, last_add_time_attr_name, timezone.now())
        else:
            setattr(self, add_in_last_hour_cnt_attr_name, add_in_last_hour_cnt + 1)

        self.save()

    def can_timenumber_action(self, model_type, threshold):
        """
            Checks if user can add som material
        """
        add_in_last_hour_cnt = getattr(self, "%s_add_in_last_hour_cnt" % model_type)
        if self._last_add_was_more_then_hour_ago(model_type) or add_in_last_hour_cnt < threshold:
            return True

        return False


