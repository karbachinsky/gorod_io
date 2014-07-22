# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField


class City(models.Model):
    """
        City class
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    short_title = models.CharField(max_length=255, null=True)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    region = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_city'

    def __unicode__(self):
        return self.name


class CityInfo(models.Model):
    """
        City info
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    text = RichTextField(max_length=25000)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_cityinfo'


class CityWelcome(models.Model):
    """
        City Welcome page for new users
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE, unique=True)
    text = RichTextField(max_length=25000)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_citywelcome'

    def get_absolute_url(self):
        """
            Http Link to this page
        """
        return reverse('gorod:welcome', kwargs={
            'city_name': self.city.name,
        })

