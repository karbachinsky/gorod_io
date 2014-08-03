# -*- coding: utf-8 -*-

from django.db import models
from gorod.models import City


class Complaint(models.Model):
    """
        Complaint class
    """

    TYPE_SPAM = 0
    TYPE_ADULT_ONLY = 1
    TYPE_UNRELIABLE = 2
    TYPE_COPYRIGHT = 3
    TYPE_OTHER = 4

    COMPLAINT_TYPES = (
        (TYPE_SPAM, u'Спам, Мошеничество'),
        (TYPE_ADULT_ONLY, u'Пост для взрослых'),
        (TYPE_UNRELIABLE, u'Недостовреная информация'),
        (TYPE_COPYRIGHT, u'Нарушение авторских прав'),
        (TYPE_OTHER, u'Другое')
    )

    email = models.EmailField()
    comment = models.TextField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    type = models.SmallIntegerField(choices=COMPLAINT_TYPES)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        app_label = 'gorod'

    def __unicode__(self):
        return self.id

