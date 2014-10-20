from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


class DONC(models.Model):
    """
        Depending object number count (comments number, answers number, etc.)
    """

    # Content-object field
    content_type = models.ForeignKey(ContentType,
        verbose_name=_('content type'),
        related_name="content_type_set_for_%(class)s"
    )
    object_pk = models.PositiveIntegerField(_('object ID'))
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    field_name = models.CharField(max_length=100)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'gorod'
        unique_together = ('object_pk', 'content_type', 'field_name')
