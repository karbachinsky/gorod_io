"""
    City payments info.
"""

from django.db import models
from gorod.models import City


class Payment(models.Model):
    """
        One payment instance
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
    title = models.CharField(max_length=255)

    class Meta:
        app_label = 'gorod'

    def __unicode__(self):
        return self.title