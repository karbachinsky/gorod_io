# -*- coding: utf-8 -*-

from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey

from gorod.models import City


class OrganizationCategoryManager(models.Manager):
    def get_first_level_categories(self):
        """
            Filter only first level
        """
        return self.model.objects.filter(level=0)


class OrganizationCategory(MPTTModel):
    """
        Organization category tree
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_organizationcategory'
        verbose_name_plural = 'organization categories'

    objects = OrganizationCategoryManager()

    def __unicode__(self):
        return self.title


class OrganizationPhone(models.Model):
    """
        Organization phone list
    """
    number = models.CharField(blank=True, max_length=100)
    organization = models.ForeignKey('Organization', related_name='+')

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_organizationphone'

    def __unicode__(self):
        return self.number


class OrganizationAddress(models.Model):
    """
        Organization addresses list
    """
    address = models.CharField(max_length=255, blank=True)
    organization = models.ForeignKey('Organization', related_name='+')

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_organizationaddress'

    def __unicode__(self):
        return self.address


class OrganizationSchedule(models.Model):
    """
        Organization day schedule
    """
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

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_organizationschedule'

    @property
    def day_name_rus(self):
        try:
            return filter(lambda x: x[0] == self.day_name, self.__class__._days)[0][1]
        except KeyError:
            return self.day_name

    def __unicode__(self):
        return self.day_name + self.time_from + self.time_to


class OrganizationManager(models.Manager):
    def get_all_published(self):
        return self.model.objects.all()


class Organization(models.Model):
    """
        City organization class
    """
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = TreeForeignKey(OrganizationCategory, on_delete=models.PROTECT)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    name = models.CharField(max_length=255)
    description = RichTextField(max_length=25000, blank=True)
    web_site = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    logo = models.ImageField(max_length=255, upload_to='organizations/', default='', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # Link on yandex map constructor
    map_link = models.CharField(blank=True, max_length=450, null=True,
                                help_text="Yandex map constructor link from: http://api.yandex.ru/maps/tools/constructor/")
    #twitter_link = models.URLField(blank=True)
    #vk_link = models.URLField(blank=True)
    #ok_link = models.URLField(blank=True)
    #my_mail_link = models.URLField(blank=True)

    objects = OrganizationManager()

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_organization'

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

    def get_absolute_url(self):
        """
            Http Link to this organization
        """
        return reverse('gorod:organization', kwargs={
            'city_name': self.city.name,
            'organization_id': self.id
        })

    url = property(get_absolute_url)

    def __unicode__(self):
        return self.name


