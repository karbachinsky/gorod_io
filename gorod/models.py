from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

from mptt.models import MPTTModel, TreeForeignKey

import gorod.fields.schedule

import validators


class City(models.Model):
    """ City class """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    wallpaper = models.ImageField(max_length=255, upload_to='wallpapers/', default='')

    def __unicode__(self):
        return self.name


class CityInfo(models.Model):
    """ Module About or city info """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    text = RichTextField(max_length=25000)


class ArticleRubric(models.Model):
    """ ArticleRubric class """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    """ Article class """
    title = models.CharField(max_length=255)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    rubric = models.ForeignKey(ArticleRubric, default=1)
    user = models.ForeignKey(User) 
    picture = models.ImageField(max_length=255, upload_to='pictures/', default='', blank=True)
    #text = models.TextField()
    text = RichTextField()
    #text = HTMLField()

    def __unicode__(self):
        return self.title


class OrganizationCategory(MPTTModel):
    """Organization category tree"""
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return mark_safe("%s%s" % ("&nbsp;" * 4 * self.level ,self.title))


class Organization(models.Model):
    """ City organization class """
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User)
    logo = models.ImageField(max_length=255, upload_to='organizations/', default='', blank=True)
    category = models.ForeignKey(OrganizationCategory, on_delete=models.PROTECT)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    web_site = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    #map_link = models.CharField(blank=True, max_length=255)
    twitter_link = models.URLField(blank=True)
    vk_link = models.URLField(blank=True)
    ok_link = models.URLField(blank=True)
    my_mail_link = models.URLField(blank=True)
    schedule_weekdays = gorod.fields.schedule.DayScheduleField(blank=True, verbose_name='Schedule Weekdays')
    schedule_weekends = gorod.fields.schedule.DayScheduleField(blank=True, verbose_name='Schedule Weekends')

    def __unicode__(self):
        return self.name


