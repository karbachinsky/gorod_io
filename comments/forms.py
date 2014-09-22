# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from django.utils.translation import ugettext as _

from django.conf import settings
from django.contrib.comments.forms import CommentForm
from models import MPTTComment


class MPTTCommentForm(CommentForm):
    def __init__(self, *args, **kwargs):
        super(MPTTCommentForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs['placeholder'] = _(u"Комментарий")

    parent = forms.ModelChoiceField(
        queryset=MPTTComment.objects.all(),
        required=False,
        widget=forms.HiddenInput
    )
    comment = forms.CharField(
        label=_(u"Комментарий"),
        widget=forms.Textarea,
        max_length=settings.COMMENT_MAX_LENGTH,
        error_messages=dict(
            required=_(u"Введите комментарий")
        )
    )
    honeypot = forms.CharField(
        required=False,
        label=_('If you enter anything in this field  \
                your comment will be treated as spam')
    )

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return MPTTComment

    def get_comment_create_data(self):
        # Use the data of the superclass, and add in the parent field field
        data = super(MPTTCommentForm, self).get_comment_create_data()
        data['parent'] = self.cleaned_data['parent']
        return data

    def clean_honeypot(self):
        """Check that nothing's been entered into the honeypot."""
        value = self.cleaned_data["honeypot"]
        if value:
            raise forms.ValidationError(self.fields["honeypot"].label)
        return value