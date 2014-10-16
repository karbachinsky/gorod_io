# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, HiddenInput, TextInput
from django.utils.translation import ugettext as _
from django.utils.html import escape

from gorod.models import HubAnswer, HubQuestion


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


class HubQuestionAddForm(ModelForm):
    """
        Hub question add form
    """

    class Meta:
        model = HubQuestion
        fields = ['category', 'question', 'description']
        localized_fields = ['category', 'question', 'description']
        widgets = {
            'question': TextInput(attrs={'placeholder': 'Введите ваш вопрос', 'autocomplete':'off'}),
            'description': Textarea(attrs={'placeholder': 'Описание вопроса'}),
        }
        error_messages = {
            'question': {
                'required': _(u"Введите вопрос"),
                'min_length': _(u"Длина вопроса должна быть не менее 3 символов")
            },
            'category': {
                'required': _(u"Выберите категорию")
            }
        }

