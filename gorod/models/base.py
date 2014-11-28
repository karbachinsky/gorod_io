# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import capfirst

from gorod.utils.word_processor import WordProcessor

from ckeditor.fields import RichTextField


class City(models.Model):
    """
        City class
    """
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_gent = models.CharField(max_length=255, null=True, blank=True)
    short_title = models.CharField(max_length=255, null=True)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)
    region = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'gorod'
        db_table = 'gorod_city'
        verbose_name_plural = 'cities'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title_gent:
            self._set_title_gent()
        super(City, self).save(*args, **kwargs)

    def _set_title_gent(self):
        wordproc = WordProcessor()
        self.title_gent = capfirst(wordproc.inflect(self.title, 'gent'))