# -*- coding: utf-8 -*-

from django.forms import ModelForm, Textarea, EmailInput, RadioSelect
from gorod.models import Complaint


class ComplaintAddForm(ModelForm):
    """
        Complaint add form
    """

    class Meta:
        model = Complaint
        fields = ['email', 'comment', 'type', 'city', 'url']
        localized_fields = ['email', 'comment', 'type', 'city', 'url']
        widgets = {
            'type': RadioSelect(attrs={'placeholder': 'Текст'}),
            'email': EmailInput(attrs={'placeholder': 'Введите ваш email'}),
            'comment': Textarea(attrs={'placeholder': 'Комментарий'}),
        }

