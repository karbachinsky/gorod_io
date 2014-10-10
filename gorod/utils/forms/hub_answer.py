# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, HiddenInput
from django.utils.translation import ugettext as _
from django.utils.html import escape

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
                'min_length': _(u"Длина ответа должна быть не менее 3 символов")
            }
        }

    def clean_text(self):
        text = escape(self.cleaned_data.get('text', ''))
        return text

