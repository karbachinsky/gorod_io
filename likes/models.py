from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Like(models.Model):
    """
        One like representation
    """

    # Content-object field
    content_type = models.ForeignKey(ContentType,
        verbose_name=_('content type'),
        related_name="content_type_set_for_%(class)s"
    )
    object_pk = models.PositiveIntegerField(_('object ID'))
    content_object = generic.GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    ctime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # Positive and negative likes
    is_positive = models.BooleanField(default=True)

    class Meta:
        app_label = 'gorod'