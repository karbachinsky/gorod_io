# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin import widgets
from django.utils.translation import ugettext as _

from django.conf import settings
from models import Like


class LikeForm(forms.ModelForm):
    class Meta:
        #fields = ['picture', 'title', 'rubric', 'text']
        model = Like

    #def __init__(self, *args, **kwargs):
    #    super(LikeForm, self).__init__(*args, **kwargs)