# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, HiddenInput
from django.utils.translation import ugettext as _

from gorod.models import HubAnswer


class HubAnswerAddForm(ModelForm):
    """
        Hub answer add form
    """

    class Meta:
        model = HubAnswer
        fields = ['question', 'text']
        widgets = {
            'text': Textarea(attrs={'placeholder': 'Введите ответ на вопрос'}),
            'question': HiddenInput(),
        }
        error_messages = {
            'text': {
                'required': _(u"Введите ответ"),
            }
        }

