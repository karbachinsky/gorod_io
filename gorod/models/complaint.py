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

    _COMPLAINT_TYPES = (
        (TYPE_SPAM, 'Спам, Мошеничество'),
        (TYPE_ADULT_ONLY, 'Пост для взрослых'),
        (TYPE_UNRELIABLE, 'Недостовреная информация'),
        (TYPE_COPYRIGHT, 'Нарушение авторских прав'),
        (TYPE_OTHER, 'Другое')
    )

    email = models.EmailField()
    comment = models.TextField(max_length=1000)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    url = models.URLField()
    type = models.SmallIntegerField(choices=_COMPLAINT_TYPES)
    add_date = models.DateTimeField(editable=False, auto_now_add=True)

    class Meta:
        app_label = 'gorod'

    def __unicode__(self):
        return self.id

