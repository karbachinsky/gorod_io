from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse, NoReverseMatch

from gorod.models.base import City


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

    #def __unicode__(self):
    #    return self.email
