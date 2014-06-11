# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.core.validators import RegexValidator
from django.conf import settings

from mptt.models import MPTTModel, TreeForeignKey

# -*- coding: utf-8 -*-


class City(models.Model):
    """ City class """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    region = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name


class User(AbstractUser):
    """
        Custom User: adding city and other
        profile information to default Django User model.
    """
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.SET_NULL)
    avatar = models.CharField(max_length=255, blank=True, null=True)

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
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    picture = models.ImageField(max_length=255, upload_to='pictures/', default='', blank=True)
    text = RichTextField()

    def __unicode__(self):
        return self.title


class OrganizationCategory(MPTTModel):
    """ Organization category tree """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.title
        #return mark_safe("%s%s" % ("&nbsp;" * 4 * self.level, self.title))


class OrganizationPhone(models.Model):
    """ Organization phone list """
    number = models.CharField(blank=True, max_length=100)
    organization = models.ForeignKey('Organization', related_name='+')

    def __unicode__(self):
        return self.number


class OrganizationAddress(models.Model):
    """ Organization addresses list """
    address = models.CharField(max_length=255, blank=True)
    organization = models.ForeignKey('Organization', related_name='+')

    def __unicode__(self):
        return self.address


class OrganizationSchedule(models.Model):
    """ Organization day schedule """
    _time_validator = RegexValidator(
        regex='^[0-9]{1,2}:[0-9]{1,2}$',
        message='Time must be in format hh:mm',
    )

    _days = [
        ('weekdays', u'Будние дни'),
        ('weekend', u'Выходные'),
        ('monday', u'Понедельник'),
        ('tuesday', u'Вторник'),
        ('wednesday', u'Среда'),
        ('thursday', u'Четверг'),
        ('friday', u'Пятница'),
        ('saturday', u'Суббота'),
        ('sunday', u'Воскресенье'),
    ]

    time_from = models.CharField(max_length=255, blank=False, validators=[_time_validator],
                                 help_text='format: 9:00')
    time_to = models.CharField(max_length=255, blank=False, validators=[_time_validator],
                               help_text='format: 16:00')
    day_name = models.CharField(choices=_days, max_length=100, default='weekdays')
    organization = models.ForeignKey('Organization', related_name='+')

    @property
    def day_name_rus(self):
        try:
            return filter(lambda x: x[0] == self.day_name, self.__class__._days)[0][1]
        except:
            return self.day_name

    def __unicode__(self):
        return self.day_name + self.time_from + self.time_to


class Organization(models.Model):
    """ City organization class """
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    logo = models.ImageField(max_length=255, upload_to='organizations/', default='', blank=True)
    category = TreeForeignKey(OrganizationCategory, on_delete=models.PROTECT)
    web_site = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    #map_link = models.CharField(blank=True, max_length=255)
    twitter_link = models.URLField(blank=True)
    vk_link = models.URLField(blank=True)
    ok_link = models.URLField(blank=True)
    my_mail_link = models.URLField(blank=True)
    description = RichTextField(max_length=25000, blank=True)

    def _get_phones(self):
        """
            List of organization phone objects
        """
        return OrganizationPhone.objects.filter(organization=self.id).all

    phones = property(_get_phones)

    def _get_addresses(self):
        """
            List of organization address objects
        """
        return OrganizationAddress.objects.filter(organization=self.id).all

    addresses = property(_get_addresses)

    def _get_schedules(self):
        """
            Organization schedules
        """
        return OrganizationSchedule.objects.filter(organization=self.id)

    schedules = property(_get_schedules)

    def _get_category_breadcrumbs(self):
        """
            List of categories from root to current category leaf
        """
        return map(lambda x: x, self.category.get_ancestors(include_self=True))

    category_breadcrumbs = property(_get_category_breadcrumbs)

    def __unicode__(self):
        return self.name


